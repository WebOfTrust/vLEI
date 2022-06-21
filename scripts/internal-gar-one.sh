#!/bin/bash

kli init --name intgar1 --salt 0AMDEyMzQ1Njc4OWxtbm9AbC --nopasscode --config-dir ./scripts --config-file demo-witness-oobis
kli incept --name intgar1 --alias intgar1 --file scripts/single-sig-incept.json

kli oobi resolve --name intgar1 --alias intgar1 --oobi-alias "GLEIF Root" --oobi http://20.121.171.161:7723/.well-known/keri/oobi/gleif-root
# kli oobi resolve --name intgar1 --alias intgar1 --oobi-alias intgar2 --oobi http://20.124.165.46:5642/oobi/E7OkfLb9BM6DL7N8RCvKmTGrdg_LlUI3jqNcyZqSMdOE/witness/Boq71an-vhU6DtlZzzJF7yIqbQxb56rcxeB0LppxeDOA

echo "intgar1 OOBIs:"
kli oobi generate --name intgar1 --alias intgar1 --role witness
echo ""

# kli challenge respond --name intgar1 --alias intgar1 --recipient "GLEIF Root" --words ""
# kli multisig incept --name intgar1 --alias intgar1 --group "Internal GAR" --file scripts/internal-gar-incept.json
