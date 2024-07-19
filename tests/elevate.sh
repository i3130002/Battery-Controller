[ "$UID" -eq 0 ] || exec sudo bash "$0" "$@"

whoami
sleep(5)