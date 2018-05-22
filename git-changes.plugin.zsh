script_name=$0
script_full_path=$(dirname "$0")

function git-changes() {
    python $script_full_path/changes.py;
}
