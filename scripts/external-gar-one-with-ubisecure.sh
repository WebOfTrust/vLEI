# Ensure that UbiSecure Checks contacts and has GLEIF External

# Paste the following challenge words in Zoom Chat
# also guard buffalo scatter useless bench into fortune cheese solid oblige neither

# Capture Multisig AID from logs of QAR POD, update extgar-delegate-icp-anchor.json, update OOBIs, send to Griff

# Approve QVI Delegation
# kli multisig interact --name extgar1 --alias "External GAR" --data @scripts/extgar-delegate-icp-anchor.json

# Resolve UbiSecure OOBI
# kli oobi resolve --name extgar1 --alias extgar1 --oobi-alias "UbiSecure QVI" --oobi http://20.124.164.251:5642/oobi/E0m0vlIMbPVbNVfPTH3NcLW0iagpyke_4OVZN7YNFLkE/witness/B4tbPLI_TEze0pzAA-X-gewpdg22yfzN8CdKKIF5wETM

##### Create Revocation Registry
##### kli vc registry incept --name extgar1 --alias "External GAR" --registry-name vLEI --nonce AHSNDV3ABI6U8OIgKaj3aky91ZpNL54I5_7-qwtC6q2s

##### Resolve Credential Schema
##### kli oobi resolve --name extgar1 --alias extgar1 --oobi-alias vc --oobi http://20.121.171.161:7723/oobi/EWCeT9zTxaZkaC_3-amV2JtG6oUxNA36sCC0P5MI7Buw

# Issue QVI Credential from GLEIF External
# kli vc issue --name extgar1 --alias "External GAR" --registry-name vLEI --schema EWCeT9zTxaZkaC_3-amV2JtG6oUxNA36sCC0P5MI7Buw --recipient "UbiSecure QVI" --data @scripts/qvi-data.json

# SEND GRIF CONTENTS OF credential.json