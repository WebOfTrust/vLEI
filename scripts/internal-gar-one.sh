#!/bin/bash

kli init --name intgar1 --salt 0AMDEyMzQ1Njc4OWxtbm9AbC --nopasscode --config-dir ./scripts --config-file demo-witness-oobis
kli incept --name intgar1 --alias intgar1 --file scripts/single-sig-incept.json

kli oobi resolve --name intgar1 --alias intgar1 --oobi-alias "GLEIF Root" --oobi http://20.121.171.161:7723/.well-known/keri/oobi/gleif-root
# kli oobi resolve --name intgar1 --alias intgar1 --oobi-alias intgar2 --oobi http://127.0.0.1:5642/oobi/ELS0QzVVwZiGAs_IzDaIjMmscsRfE34apLICJNgC55a8/witness/BGKVzj4ve0VSd8z_AmvhLg4lqcC_9WYX90k03q-R_Ydo

echo "intgar1 OOBIs:"
kli oobi generate --name intgar1 --alias intgar1 --role witness
echo ""

# kli multisig incept --name intgar1 --alias intgar1 --group "External GAR" --file scripts/demo/internal-gar-incept.json
