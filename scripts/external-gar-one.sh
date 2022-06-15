#!/bin/bash

kli init --name extgar1 --salt 0AMDEyMzQ1Njc4OWxtbm9wcQ --nopasscode --config-dir ./scripts --config-file demo-witness-oobis
kli incept --name extgar1 --alias extgar1 --file tests/app/cli/commands/multisig/multisig-1-sample.json

kli oobi resolve --name extgar1 --alias extgar1 --oobi-alias "GLEIF Root" --oobi http://127.0.0.1:7723/.well-known/keri/oobi/gleif-root
kli oobi resolve --name extgar1 --alias extgar1 --oobi-alias extgar2 --oobi http://127.0.0.1:5642/oobi/Eyzi1Yme3BEbu2h8HUf7fqeXjBQ-yjE6YW7OFSH3WgyY/witness/BGKVzj4ve0VSd8z_AmvhLg4lqcC_9WYX90k03q-R_Ydo

echo "ExtGAR1 OOBIs:"
kli oobi generate --name extgar1 --alias extgar1 --role witness
echo ""

# kli multisig incept --name extgar1 --alias extgar1 --group "External GAR" --file scripts/demo/external-gar-incept.json
