#!/bin/bash

kli init --name extgar2 --salt 0AMDEyMzQ1Njc4OWdoaWpsaw --nopasscode --config-dir ./scripts --config-file demo-witness-oobis
kli incept --name extgar2 --alias extgar2 --file tests/app/cli/commands/multisig/multisig-2-sample.json

kli oobi resolve --name extgar2 --alias extgar2 --oobi-alias "GLEIF Root" --oobi http://127.0.0.1:7723/.well-known/keri/oobi/gleif-root
kli oobi resolve --name extgar2 --alias extgar2 --oobi-alias extgar1 --oobi http://127.0.0.1:5642/oobi/E2q4geQjWVAIScE08i_ey_2DgG32rEwz5UlwO_Gd7adA/witness/BGKVzj4ve0VSd8z_AmvhLg4lqcC_9WYX90k03q-R_Ydo

echo "ExtGAR2 OOBIs"
kli oobi generate --name extgar2 --alias extgar2 --role witness

# kli multisig incept --name extgar2 --alias extgar2 --group "External GAR" --file scripts/demo/external-gar-incept.json
