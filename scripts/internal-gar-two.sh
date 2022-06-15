#!/bin/bash

kli init --name intgar2 --salt 0AMDEyMzQ1Njc4OWdoaWpEfG --nopasscode --config-dir ./scripts --config-file demo-witness-oobis
kli incept --name intgar2 --alias intgar2 --file tests/app/cli/commands/multisig/multisig-2-sample.json

kli oobi resolve --name intgar2 --alias intgar2 --oobi-alias "GLEIF Root" --oobi http://127.0.0.1:7723/.well-known/keri/oobi/gleif-root
kli oobi resolve --name intgar2 --alias intgar2 --oobi-alias intgar1 --oobi http://127.0.0.1:5642/oobi/EOVXzTuvdfVtDt6nXiOWFt97QM3jG1x-Mz_MfL8kyRQc/witness/BGKVzj4ve0VSd8z_AmvhLg4lqcC_9WYX90k03q-R_Ydo

echo ""
echo "intgar2 OOBIs"
kli oobi generate --name intgar2 --alias intgar2 --role witness

# kli multisig incept --name intgar2 --alias intgar2 --group "External GAR" --file scripts/demo/internal-gar-incept.json
