---
summary: Public data-source APIs for live layers on the vr-brain Earth globe — weather, radar, winds, heat, air quality, quakes, fires, WiGLE wardriving, and cyber-threat feeds. Endpoints, auth, formats, rate limits.
status: active
tags: [reference, api, geospatial, vr-brain, security]
---

## Purpose

Reference for adding live data layers to the [[vr-brain - Overview|vr-brain]] Earth globe. Prioritizes **no-account** or **free-key** sources. Each fits the globe plumbing: point/vector → `Earth.LatLonToDir(lat,lon)`; raster → the `{z}/{x}/{y}` XYZ overlay path; networking via `HttpClient` on a worker thread + `ConfigFile`. Set a descriptive `User-Agent` (some sources require it). Compiled 2026-07-24. See [[High-Fidelity Planet Rendering (Godot)]] for the renderer and [[Earth - Geo Engine Rewrite]] for the layer architecture.

## 3D Mapping Platform Research

- [3D Mapping Platforms - Index](kb://06-reference-3d-mapping-platforms-3d-mapping-platforms-index) - comparison hub for ArcGIS Pro, Google Photorealistic 3D Tiles, Mapbox GL JS, and CesiumJS.
- [Google Maps Platform Photorealistic 3D Tiles](kb://06-reference-3d-mapping-platforms-google-maps-platform-photorealistic-3d-tiles) - official documented path for Google 3D real-world mesh via Map Tiles API and compatible 3D Tiles renderers.
- [CesiumJS 3D Geospatial Visualization](kb://06-reference-3d-mapping-platforms-cesiumjs-3d-geospatial-visualization) - reference renderer/model for 3D Tiles, terrain, imagery, and massive web-geospatial streaming.
- [Mapbox GL JS 3D Terrain and Buildings](kb://06-reference-3d-mapping-platforms-mapbox-gl-js-3d-terrain-and-buildings) - web map stack for terrain, vector styling, and building/polygon extrusion.
- [Esri ArcGIS Pro 3D GIS](kb://06-reference-3d-mapping-platforms-esri-arcgis-pro-3d-gis) - enterprise GIS authoring/analysis system for I3S scene layers and integrated mesh workflows.
- [Xweather MapsGL Weather Visualization](kb://06-reference-3d-mapping-platforms-xweather-mapsgl-weather-visualization) - WebGL weather SDK/reference model for animated radar, forecast, wind-particle, contour, grid, and timeline layers.
- [Eagleview Aerial Imagery and Property Intelligence](kb://06-reference-3d-mapping-platforms-eagleview-aerial-imagery-and-property-intelligence) - property-level aerial imagery, measurements, and APIs for parcel/building intelligence.
- [OpenEarth.Online 3D Mesh Export](kb://06-reference-3d-mapping-platforms-openearth-online-3d-mesh-export) - commercial mesh/panorama export workflow for AI, CG, BIM, robot simulation, and digital-twin test assets.
- [USGS EarthExplorer and The National Map Data](kb://06-reference-geospatial-usgs-earthexplorer-and-national-map-data) - official U.S. elevation, imagery, lidar, topo, hydrography, WMS/WCS/WFS/REST, and download workflows.

## Weather — NWS `api.weather.gov`

- **Auth:** no key; descriptive `User-Agent` REQUIRED (`(vr-brain-globe, guildedthorn@gmail.com)`).
- **Rate:** ~5000/hr (unofficial); supports `If-Modified-Since` → cheap 304s. Don't cache-bust.
- **Format:** GeoJSON default (`Accept: application/geo+json`). Spec: `api.weather.gov/openapi.json`.
- Alerts: `GET /alerts/active?status=actual&message_type=alert` (also `area=`, `severity=Extreme,Severe`, `event=`, `point=lat,lon`, `zone=`). Each feature: `geometry` Polygon/MultiPolygon (**may be null** → fetch `properties.affectedZones` `/zones/{type}/{id}`, cache); `properties.event/severity/urgency/effective/onset/expires/headline/areaDesc`.
- Forecast (two-step): `GET /points/{lat},{lon}` → `properties.gridId/gridX/gridY` + ready `forecast`/`forecastHourly`/`forecastGridData` URLs. Raw numeric: `/gridpoints/{wfo}/{x},{y}` (`values[]` w/ `validTime`).
- **Render:** poll alerts ~60s conditional; convert rings via `LatLonToDir` → translucent filled mesh + outline, color by severity, fade `onset`→`expires`. Validate CAP enum strings against `openapi.json`.

## Radar — IEM NEXRAD (Iowa State)

- **Host:** `mesonet.agron.iastate.edu` — no key/auth/UA. `n0q` = 8-bit composite reflectivity, 0.5 dBZ, **5-min** cadence, pre-colored PNG, transparent no-echo.
- **XYZ tiles (drop into existing overlay):** `…/cache/tile.py/1.0.0/nexrad-n0q-900913/{z}/{x}/{y}.png`
- **Animation (11-frame, 50 min):** layer name embeds `-mXXm` age: `nexrad-n0q-{900913-m50m … -m05m, 900913}`. `/cache/` = 5-min cache; `/c/` = 14-day.
- **WMS-T (absolute time / archive to 2010):** `…/cgi-bin/wms/nexrad/n0q-t.cgi?…&TIME=ISO` (`PT5M`); `GetCapabilities` for extent.
- **Alt:** NOAA nowCOAST (WMS MRMS); NCEP MRMS (~1 km/2-min GRIB2, must render).
- **Render:** low zoom (z4-5 = CONUS); preload 11 frames, cross-fade ~500 ms, refresh 5 min.

## Winds (global field for particles)

- **NOAA GFS via NOMADS/GRIB2** — the only free FULL-GRID option. No key (throttle etiquette). 0.25° = 1440×721, runs 00/06/12/18 UTC. Vars: `UGRD`/`VGRD` (`lev_10_m_above_ground` or `lev_250_mb` jet), `TMP` (`lev_2_m_above_ground`); wind m/s, temp K.
  - Filter (server subset): `nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.tHHz.pgrb2.0p25.fFFF&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.YYYYMMDD%2FHH%2Fatmos`
  - Cloud mirror: `s3://noaa-gfs-bdp-pds/`. **No mature pure-C# GRIB2 decoder** → decode offline (`wgrib2`, `cfgrib`, or `grib2json`) to a compact binary/RG-float texture.
- **cambecc/earth JSON** = de-facto ingest contract: array of 2 records `[U, V]`, each `{header, data[nx*ny]}`. `parameterNumber` 2=U 3=V; `nx/ny/lo1/la1/dx/dy/scanMode`. Value `(i,j)=data[j*nx+i]`, `lon=lo1+i*dx`, `lat=la1-j*dy`. Load U,V into one `Image` (RG float), sample in particle shader.
- **Render:** RG float texture (R=u,G=v) → advect GPU particles (nullschool technique, §patterns below).

## Temperature / heat

- **GFS `TMP`** (2 m) via NOMADS — same path as winds; data-driven color ramp you control.
- **OpenWeatherMap tiles** (free `appid`): `tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid={KEY}` (`temp_new/wind_new/precipitation_new/clouds_new/pressure_new`); 60/min, 1M/mo.
- **NASA GIBS** (no key) MODIS LST: `gibs.earthdata.nasa.gov/wmts/epsg3857/best/MODIS_Terra_Land_Surface_Temp_Day/default/{YYYY-MM-DD}/GoogleMapsCompatible_Level7/{z}/{y}/{x}.png`.
- **Render:** XYZ overlay, blend as semi-transparent emissive "heat" layer.

## Point layers (markers)

- **USGS quakes** (no key): `earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson` (`all_hour/week/month`, `2.5_day`, `significant_week`). `geometry.coordinates=[lon,lat,depth_km]`, `properties.mag/place/time/url`. Pulsing markers sized by mag.
- **NASA FIRMS fires** (free MAP_KEY in URL): `firms.modaps.eosdis.nasa.gov/api/area/csv/[KEY]/[VIIRS_SNPP_NRT]/[w,s,e,n | world]/[1-5]/[YYYY-MM-DD]`. CSV: `latitude,longitude,frp,confidence,acq_date,daynight`. 5000/10 min.
- **OpenAQ air quality** (free `X-API-Key`, v1/v2 retired 2025-01): `api.openaq.org/v3/locations?coordinates=lat,lon&radius=`. JSON, params pm25/pm10/o3/no2/so2/co. 60/min, 2000/hr.
- **OWM air pollution** (free `appid`): `api.openweathermap.org/data/2.5/air_pollution?lat=&lon=&appid=`. On-tap AQI.
- **Open-Meteo** (no key, per-point, NOT a grid): `api.open-meteo.com/v1/forecast?latitude=&longitude=&hourly=temperature_2m,wind_speed_10m,wind_direction_10m&wind_speed_unit=ms&timeformat=unixtime`. 10k/day. Use for on-tap readouts only.

## WiGLE wardriving — `api.wigle.net`

- **Auth:** HTTP Basic `base64(apiName:apiToken)` from wigle.net Account page. Console: `api.wigle.net`.
- **Search:** `GET /api/v2/network/search?latrange1={S}&latrange2={N}&longrange1={W}&longrange2={E}&resultsPerPage=100` (also `ssid`, `ssidlike`, `netid`, `encryption`, `type`, `lastupdate`; page via `searchAfter`).
- **Fields:** `trilat`/`trilong` (plot these), `ssid`, `netid` (BSSID), `encryption` (wpa2/wep/none), `type` (WIFI/BT/GSM/LTE), `lastupdate`, `channel`, `country/region/city/road`.
- **Limits (critical):** dynamic sliding daily cap, LOW for new accounts, rises with real uploads; enforced per-login AND per-IP; resets 00:00 US/Pacific; search+detail share the quota. **Tight bounding box, cap to 2-3 pages, cache hard (hours/days), dedup on `netid`.** Commercial use needs a licensed token.

## Cyber threat feeds (geolocate IP via existing GeoLite2)

Pattern: fetch feed → extract IPs → `GeoIp.Lookup` → plot with metadata popup.

- **Feodo Tracker** (botnet C2, best live geo feed, regenerated 5 min): `feodotracker.abuse.ch/downloads/ipblocklist_recommended.json`. Fields incl. `ip_address`, `port`, `status`, `as_name`, **`country`**, `first_seen`, `last_online`, `malware` (Emotet/Dridex/QakBot…). **Since 2025-06-30 abuse.ch requires a free `Auth-Key` header** (one key from `auth.abuse.ch`, covers ThreatFox/URLhaus/MalwareBazaar).
- **ThreatFox** (IOCs): `POST threatfox-api.abuse.ch/api/v1/` `{"query":"get_iocs","days":7}` + `Auth-Key`. Filter `ioc_type==ip:port`.
- **DShield/SANS ISC** (no auth, but **contact email in User-Agent required**): `feeds.dshield.org/feeds/topips.txt` (top 100 attacking IPs); API `isc.sans.edu/api/topips/json`.
- **AbuseIPDB** (free `Key:` header): bulk `GET api.abuseipdb.com/api/v2/blacklist`; per-IP `…/check?ipAddress=`. Fields `abuseConfidenceScore`, `countryCode`, `usageType`, `totalReports`. ~1000 checks/day free.
- **GreyNoise Community** (free `key:` header, ~50/week): `GET api.greynoise.io/v3/community/{ip}` → `noise`, `classification`, `name`. Enrichment (per-IP), not bulk.
- **CISA KEV** (no auth): `cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json`. **NOT geolocatable** — use as non-geo "active exploitation" ticker or to enrich IP alerts by matching CVE.
- **Enrichment chain:** IP feed → GeoLite2 (where) → AbuseIPDB/GreyNoise (how bad/actor) → malware family → MITRE ATT&CK (`raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json`) → KEV/NVD (`services.nvd.nist.gov/rest/json/cves/2.0?cveId=`) for CVE severity. This turns a dot into an "alert".
- **Attack maps:** the famous ones (Fortinet/Kaspersky/Norse) have no open feed — build your own arcs from Feodo + DShield + AbuseIPDB.

## Visualization patterns

- **Wind particles:** vector field on equirect grid; velocity = bilinear of 4 cells (u,v separately). CPU (nullschool, ~5k particles): particle array `{pos, age}`, advect, draw short segments, fade trails via low-alpha full-canvas fill, respawn on max-age/null-cell. GPU (webgl-wind, ~1M): positions in a state texture, ping-pong update shader (manual 4-tap bilinear + `cos(lat)` correction + speed-based drop-rate respawn), draw pass colors by speed, trails = redraw dimmed previous frame. Godot: `GPUParticles3D`+process shader, or compute-shader ping-pong; `RGF` wind texture.
- **Scalar → heatmap:** color LUT (256-entry 1-D texture / `GradientTexture`) indexed by normalized value; sphere shader `albedo=texture(ramp, vec2(norm_scalar,0))`.
- **Equirect→sphere:** `u=lon/360`, `v=lat/180`.

## Recommended starting set (no account)

1. NWS alerts (vector polygons, high payoff). 2. IEM `n0q` radar (XYZ, 5-min loop). 3. USGS quakes (trivial GeoJSON). 4. GFS winds (flagship particle layer, offline decode). Free-key extras: OWM/GIBS heat, OpenAQ, FIRMS, WiGLE, abuse.ch.

## Related

- [[High-Fidelity Planet Rendering (Godot)]]
- [[Earth - Geo Engine Rewrite]]
- [[vr-brain - Overview]]
