# coding: utf-8
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -------------------------------------------------------------------------
import pytest
from azure.messaging.webpubsubservice.aio import WebPubSubServiceClient
from azure.messaging.webpubsubservice._operations._operations import build_send_to_all_request
from azure.core.credentials import AzureKeyCredential
from devtools_testutils.fake_async_credential import AsyncFakeCredential

@pytest.mark.asyncio
async def test_reverse_proxy_endpoint_redirection():
    def _callback(pipeline_request):
        assert pipeline_request.http_request.url.startswith("https://apim.contoso.com/")
        raise ValueError("Success!")
    wps_endpoint = "https://wps.contoso.com/"
    apim_endpoint = "https://apim.contoso.com/"
    credential = AzureKeyCredential("abcdabcdabcdabcdabcdabcdabcdabcd")
    request = build_send_to_all_request("Hub", content='test_webpubsub_send_request', content_type='text/plain')
    async with WebPubSubServiceClient(wps_endpoint, "Hub", credential, reverse_proxy_endpoint=apim_endpoint) as client:
        with pytest.raises(ValueError) as ex:
            await client.send_request(request, raw_request_hook=_callback)
        assert "Success!" in str(ex.value)

@pytest.mark.asyncio
async def test_reverse_proxy_endpoint_redirection_identity():
    def _callback(pipeline_request):
        assert pipeline_request.http_request.url.startswith("https://apim.contoso.com/")
        raise ValueError("Success!")
    wps_endpoint = "https://wps.contoso.com/"
    apim_endpoint = "https://apim.contoso.com/"
    credential = AsyncFakeCredential()
    request = build_send_to_all_request('Hub', content='test_webpubsub_send_request', content_type='text/plain')
    async with WebPubSubServiceClient(wps_endpoint, "Hub", credential, reverse_proxy_endpoint=apim_endpoint) as client:
        with pytest.raises(ValueError) as ex:
            await client.send_request(request, raw_request_hook=_callback)
        assert "Success!" in str(ex.value)
