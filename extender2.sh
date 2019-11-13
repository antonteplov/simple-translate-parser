#!/bin/bash
cat  > /dev/shm/tmp1
cat /dev/shm/tmp1 | awk -F'/' '{ if(NF>1) print $1," ",$2,"" }'
cat /dev/shm/tmp1 | awk -F'/' '{ if(NF>2) print $1," ",$3,"" }'
cat /dev/shm/tmp1 | awk -F'/' '{ if(NF>3) print $1," ",$4,"" }'
cat /dev/shm/tmp1 | awk -F'/' '{ if(NF>4) print $1," ",$5,"" }'
cat /dev/shm/tmp1 | awk -F'/' '{ if(NF>5) print $1," ",$6,"" }'
cat /dev/shm/tmp1 | awk -F'/' '{ if(NF>6) print $1," ",$7,"" }'
cat /dev/shm/tmp1 | awk -F'/' '{ if(NF>7) print $1," ",$8,"" }'
cat /dev/shm/tmp1 | awk -F'/' '{ if(NF>8) print $1," ",$9,"" }'
cat /dev/shm/tmp1 | awk -F'/' '{ if(NF>9) print $1," ",$10,"" }'
cat /dev/shm/tmp1 | awk -F'/' '{ if(NF>10) print $1," ",$11,"" }'
cat /dev/shm/tmp1 | awk -F'/' '{ if(NF>11) print $1," ",$12,"" }'
cat /dev/shm/tmp1 | awk -F'/' '{ if(NF>12) print $1," ",$13,"" }'
