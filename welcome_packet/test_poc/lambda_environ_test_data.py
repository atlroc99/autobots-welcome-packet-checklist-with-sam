import os
data = {
    "AWS_LAMBDA_FUNCTION_MEMORY_SIZE": "128",
    "_HANDLER": "get_checklist_by_dealer_name.lambda_handler",
    "AWS_ACCOUNT_ID": "NOT TODAY FOO",
    "HOME": "/root",
    "SHLVL": "0",
    "AWS_ACCESS_KEY_ID": "NOT TODAY FOO-AWS_ACCESS_KEY_ID",
    "AWS_LAMBDA_FUNCTION_HANDLER": "get_checklist_by_dealer_name.lambda_handler",
    "AWS_REGION": "us-west-1",
    "TZ": ":/etc/localtime",
    "LAMBDA_RUNTIME_DIR": "/var/runtime",
    "LANG": "en_US.UTF-8",
    "AWS_SECRET_ACCESS_KEY": "NOT TODAY FOO-AWS_SECRET_ACCESS_KEY",
    "PWD": "/var/task",
    "AWS_DEFAULT_REGION": "us-west-1",
    "PATH": "/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin",
    "AWS_LAMBDA_FUNCTION_NAME": "GetChecklistByDealerNameFunction",
    "AWS_EXECUTION_ENV": "AWS_Lambda_python3.8",
    "AWS_LAMBDA_RUNTIME_API": "127.0.0.1: 9001",
    "AWS_LAMBDA_LOG_STREAM_NAME": "$LATEST",
    "AWS_LAMBDA_LOG_GROUP_NAME": "aws/lambda/GetChecklistByDealerNameFunction",
    "LAMBDA_TASK_ROOT": "/var/task",
    "LD_LIBRARY_PATH": "/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib",
    "AWS_LAMBDA_FUNCTION_TIMEOUT": "7",
    "AWS_SESSION_TOKEN": "FSJAFSAJFSLAFJLSAJFSLAJFLSAJFLSAJFSAFJLSAJFLSAJFLSJFLJFJSALFJSAFJSALFIOJLFJFLA",
    "AWS_SAM_LOCAL": "false",
    "HOSTNAME": "AWS_HOST_NAME",
    "AWS_LAMBDA_FUNCTION_VERSION": "$LATEST",
    "PYTHONPATH": "/var/runtime"
}

print(os.environ.get('AWS_SAM_LOCAL'))