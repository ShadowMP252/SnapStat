#!/bin/bash

set -e

DATE=$(date +"%Y-%m-%d_%H-%M-%S")

COMMIT_MESSAGE="SnapStat - $DATE"

while [[ $# -gt 0 ]]; do
    case $1 in
        --changes)
            shift
            if [[ -n "$1" ]]; then
                COMMIT_MESSAGE="$COMMIT_MESSAGE - $1"
                shift
            else
                echo "Error: --changes requires an argument."
                exit 1
            fi
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
    esac
done

git add .
git commit -m "$COMMIT_MESSAGE"
git push