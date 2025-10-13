.PHONY: push-all, build, publish

VERSION=1.0.1
IMAGE_NAME=gleif/vlei
LATEST_TAG=$(IMAGE_NAME):latest
VERSION_TAG=$(IMAGE_NAME):$(VERSION)

push-all:
	@docker push $(IMAGE_NAME) --all-tags

build:
	@docker build \
		--platform=linux/amd64,linux/arm64 \
		-f container/Dockerfile \
		--tag $(LATEST_TAG) \
		--tag $(VERSION_TAG) \
		.

publish:
	@docker push $(IMAGE_NAME):latest
	@docker push $(IMAGE_NAME):$(VERSION)
