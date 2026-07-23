---
summary: Keep short command references that are useful enough to reuse but not large enough to deserve their own notes.
status: active
tags: [reference]
---

## Purpose

Keep short command references that are useful enough to reuse but not large enough to deserve their own notes. General, accurate commands only — anything host-specific belongs in the host's own note.

## NixOS

```bash
# Rebuild the current host from the flake and switch
sudo nixos-rebuild switch --flake .#<host>

# Build without switching (dry activation / test)
sudo nixos-rebuild test --flake .#<host>
sudo nixos-rebuild build --flake .#<host>

# Build a config for a remote host and deploy it over SSH
nixos-rebuild switch --flake .#<host> --target-host root@<host> --use-remote-sudo

# Update flake inputs (nixpkgs, home-manager, ...)
nix flake update            # all inputs
nix flake lock --update-input nixpkgs

# Inspect / garbage collect the store
nix-store --gc
sudo nix-collect-garbage -d          # also delete old generations
nix profile history

# Roll back the last activation
sudo nixos-rebuild switch --rollback

# Search for a package
nix search nixpkgs <term>

# Enter a throwaway shell with a package
nix shell nixpkgs#<pkg>
```

See [Rebuild and Host Selection](kb://02-systems-nixos-rebuild-and-host-selection).

## Git

```bash
git status -sb                       # compact status + branch
git log --oneline --graph --decorate --all
git switch -c <branch>               # create + switch
git restore --staged <file>          # unstage
git restore <file>                   # discard working change
git commit --amend --no-edit         # fold into last commit
git rebase --onto <new> <old> <br>   # replant a branch
git stash push -m "wip"; git stash pop
git reflog                           # recover "lost" commits
git remote -v
```

## systemd / journal

```bash
systemctl status <unit>
systemctl restart <unit>
systemctl --user status <unit>       # user services
journalctl -u <unit> -f              # follow
journalctl -b -p err                 # this boot, errors+
journalctl --since "1 hour ago"
systemd-analyze blame                # boot time by unit
```

## SSH / networking

```bash
ssh -J jump@bastion user@internal    # ProxyJump through a bastion
ssh -L 8080:localhost:80 host        # local port forward
ssh -R 9000:localhost:9000 host      # remote port forward
ssh-copy-id user@host
ss -tulpn                            # listening sockets
ip -br a                             # brief interface addresses
ip route
mtr <host>                           # traceroute + ping combined
```

See [SSH Access](kb://05-network-ssh-access) and [Remote Recovery](kb://05-network-remote-recovery).

## WireGuard

```bash
sudo wg show                         # peers, handshakes, transfer
sudo wg-quick up wg0
sudo wg-quick down wg0
wg genkey | tee priv | wg pubkey > pub
```

See [WireGuard - Road Warrior](kb://05-network-wireguard-road-warrior).

## ZFS / TrueNAS

```bash
zpool status -v
zpool list
zfs list -o name,used,avail,mountpoint
zfs list -t snapshot
zpool scrub <pool>
zfs get compressratio <dataset>
```

See [TrueNAS](kb://03-devices-truenas).

## RTL-SDR / radio

```bash
rtl_test -t                          # confirm dongle + tuner
rtl_fm -f 162.55M -M fm -s 22050 | play -r 22050 -t raw -e s -b 16 -c 1 -
SoapySDRUtil --find                  # enumerate SDR devices
```

See [Amateur Radio and SDR](kb://10-hobbies-amateur-radio-and-sdr).

## Related

- [Software Map](kb://01-maps-software-map)
- [NixOS Map](kb://01-maps-nixos-map)
- [Network Map](kb://01-maps-network-map)
- [Reference Map](kb://01-maps-reference-map)
