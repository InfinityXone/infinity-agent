#!/bin/bash
cd /mnt/data/infinity-agent
git add .
git commit -m "Auto-push from Infinity Agent $(date)"
git push origin main
