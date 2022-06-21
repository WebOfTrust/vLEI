# Receive UbiSecure MS AID from Phil, paste in extgar-delegate-icp-anchor.json 'i' and 'd', update OOBIS below

# Approve QVI Delegation
# kli multisig interact --name extgar2 --alias "GLEIF External" --data @scripts/extgar-delegate-icp-anchor.json

# Resolve UbiSecure OOBI
# kli oobi resolve --name extgar2 --alias extgar2 --oobi-alias "UbiSecure QVI" --oobi http://20.124.164.251:5642/oobi/<INSERT UBISECURE MS AID HERE>/witness/B4tbPLI_TEze0pzAA-X-gewpdg22yfzN8CdKKIF5wETM

# Create Revocation Registry
# kli vc registry incept --name extgar2 --alias "GLEIF External" --registry-name vLEI --nonce AHSNDV3ABI6U8OIgKaj3aky91ZpNL54I5_7-qwtC6q2s

# Resolve Credential Schema
# kli oobi resolve --name extgar2 --alias extgar2 --oobi-alias vc --oobi http://20.121.171.161:7723/oobi/EWCeT9zTxaZkaC_3-amV2JtG6oUxNA36sCC0P5MI7Buw

# Issue QVI Credential from GLEIF External

# GET CONTENTS OF FILE FROM PHIL CHAT, CREATE credential.json and run:

# kli vc issue --name extgar2 --alias "GLEIF External" --credential @./credential.json
