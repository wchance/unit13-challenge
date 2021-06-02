            initial_recommendation = "80% bonds (AGG), 20% equities (SPY)"
        elif risk_level == "Low":
            initial_recommendation = "60% bonds (AGG), 40% equities (SPY)"
        elif risk_level == "Medium":
            initial_recommendation = "40% bonds (AGG), 60% equities (SPY)"
        elif risk_level == "High":
            initial_recommendation = "20% bonds (AGG), 80% equities (SPY)"
        elif risk_level == "Very High":
            initial_recommendation = "0% bonds (AGG), 100% equities (SPY)"
    ### YOUR FINAL INVESTMENT RECOMMENDATION CODE ENDS HERE ###

    if source == "DialogCodeHook":
        # Perform basic validation on the supplied input slots.
        # Use the elicitSlot dialog action to re-prompt
        # for the first violation detected.
        
        ### YOUR DATA VALIDATION CODE STARTS HERE ###
        if age is not None and age == 50:
            #if (age < 1) or (age > 65):
            return {'error': 'You are not the recommended age'}
        #if investment_amount is not None:
        #    if (investment_amount < 5000):
        #        print ("You must invest a minimum of $5000.00")
        ### YOUR DATA VALIDATION CODE ENDS HERE ###

        
        # Fetch current session attibutes
        output_session_attributes = intent_request["sessionAttributes"]

        return delegate(output_session_attributes, get_slots(intent_request))
        
    # Return a message with the initial recommendation based on the risk level.
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": """{} thank you for your information;
            based on the risk level you defined, my recommendation is to choose an investment portfolio with {}
            """.format(
                first_name, initial_recommendation
            ),
        },
    )


### Intents Dispatcher ###
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    intent_name = intent_request["currentIntent"]["name"]

    # Dispatch to bot's intent handlers
    if intent_name == "RecommedPortfolio":
        return recommend_portfolio(intent_request)

    raise Exception("Intent with name " + intent_name + " not supported")


### Main Handler ###
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """

    return dispatch(event)
