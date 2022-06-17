#!/bin/bash

kli init --name extgar1 --salt 0AMDEyMzQ1Njc4OWxtbm9wcQ --nopasscode --config-dir ./scripts --config-file demo-witness-oobis
kli incept --name extgar1 --alias extgar1 --file scripts/single-sig-incept.json

kli oobi resolve --name extgar1 --alias extgar1 --oobi-alias "GLEIF Root" --oobi http://20.121.171.161:7723/.well-known/keri/oobi/gleif-root
kli oobi resolve --name extgar1 --alias extgar1 --oobi-alias extgar2 --oobi http://20.124.165.46:5642/oobi/E-NIzxQ-3WXkhfBJK_ghp6neZ6RiOYELQqjYB8eCKTsA/witness/Boq71an-vhU6DtlZzzJF7yIqbQxb56rcxeB0LppxeDOA

echo "ExtGAR1 OOBIs:"
kli oobi generate --name extgar1 --alias extgar1 --role witness
echo ""

# kli multisig incept --name extgar1 --alias extgar1 --group "External GAR" --file scripts/external-gar-incept.json
# kli challenge respond --name extgar1 --alias extgar1 --recipient "GLEIF Root" --words ""