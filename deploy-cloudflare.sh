#!/bin/sh
set -e
cd "$(dirname "$0")"
rm -rf dist && mkdir dist
cp -r index.html robots.txt sitemap.xml _headers images cenniki karty-katalogowe karty-katalogowe-PL dist/
npx -y wrangler@4 deploy
