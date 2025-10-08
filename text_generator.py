import boto3
import json
import os
bedrock_client = boto3.client(
    service_name='bedrock-runtime',
    region_name=os.getenv("AWS_REGION", "us-east-1")
)
model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'
prompt_text = "what is special about diwali festival?"
body = json.dumps({
    "messages": [
        {
            "role": "user",
            "content": [{"type": "text", "text": prompt_text}]
        }
    ],
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 500, 
    "temperature": 0.5,
})
try:
    response = bedrock_client.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )
    response_body = json.loads(response.get('body').read())
    generated_text = response_body['content'][0]['text']
    print("Generated Text:")
    print(generated_text)
except Exception as e:
    print(f"An error occurred: {e}")
    print("Please ensure you have requested access to the specified model in the Bedrock console.")