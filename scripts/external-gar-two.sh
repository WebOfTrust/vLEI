#!/bin/bash

kli init --name extgar2 --salt 0AMDEyMzQ1Njc4OWdoaWpsaw --nopasscode --config-dir ./scripts --config-file demo-witness-oobis
kli incept --name extgar2 --alias extgar2 --file scripts/single-sig-incept.json

kli oobi resolve --name extgar2 --alias extgar2 --oobi-alias "GLEIF Root" --oobi http://20.121.171.161:7723/.well-known/keri/oobi/gleif-root
kli oobi resolve --name extgar2 --alias extgar2 --oobi-alias extgar1 --oobi http://20.124.165.46:5642/oobi/E1kar2Jt5-6CW-rdotfKIpO6LdGAfSlluFjtfdTEc3u8/witness/Boq71an-vhU6DtlZzzJF7yIqbQxb56rcxeB0LppxeDOA

echo "ExtGAR2 OOBIs"
kli oobi generate --name extgar2 --alias extgar2 --role witness

# kli multisig incept --name extgar2 --alias extgar2 --group "External GAR" --file scripts/external-gar-incept.json
