#!/usr/bin/env bash
#
for i in $(seq 2014 2023); do
  TOTAL_CVES=$(wc -l linux-cves-${i}.csv | awk '{print $1}');
  DRIVER_CVES=$(rg "drivers/.*\.c" linux-cves-${i}.csv | awk '{print $1}' | wc -l);
  echo "${i} & $((${TOTAL_CVES}-1)) & ${DRIVER_CVES} \\\\\\\\ ";
done
