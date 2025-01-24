import json

def lambda_handler(event, context):
    # Extract numbers from the event
    num1 = event.get('num1', 0)
    num2 = event.get('num2', 0)
    
    # Calculate the sum
    result = num1 + num2
    
    # Return the result
    return {
        'statusCode': 200,
        'body': json.dumps({
            'result': result
        })
    }
