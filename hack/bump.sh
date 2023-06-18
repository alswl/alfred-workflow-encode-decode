#!/usr/bin/env bash
# This script is used to bump the version of the operator.
# It uses semtag to bump the version.

cd "$(dirname "$0")" || exit

set -e

bump_stage=$1
bump_scope=$2
bump_dry_runn=$3

if [ -z "$bump_stage" ]; then
  echo "bump stage is required"
  exit 1
fi
if [ -z "$bump_scope" ]; then
  echo "bump scope is required"
  exit 1
fi
if [ -z "$bump_dry_runn" ]; then
  echo "bump dryrun is required"
  exit 1
fi

next=$(semtag "$bump_stage" -s "$bump_scope" -o)
echo "next version: $next"

if [ "$bump_dry_runn" = "true" ]; then
  echo "dryrun: true"
  exit 0
fi

echo "dryrun: false"
echo "$next" > VERSION
git add VERSION
git commit -m "chore: Bump version to $next"

semtag "$bump_stage" -s "$bump_scope"
