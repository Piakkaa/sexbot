LineKey=$(cat ../.line)
sam build &&\
sam deploy --parameter-overrides LineKey=$LineKey
