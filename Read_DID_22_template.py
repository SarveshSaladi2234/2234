DID =Data_Identifier

SW_Variable =SW_label

request(10 03)       #Diagnostic session control in Extended subfunction

response=check_Pos_response_for(10 03)    #checking for positive response

if response.type==Positive:

    request(27 01)                        #Security access, requesting seed

    response=check_Pos_resonse_for(27 01)

    if response.type==Positive:

        send_key()

        response=check_Pos_resonse_for(27 02)

        if response.type==Positive:

            request(22 DID)#read data by identifier

            response=check_Pos_resonse_for(22 DID)

            if response.type==Positive:

                SW_Value=read_SW_variable_value(SW_Variable)

                if SW_Value==response.value:

                    print("Test Passed")

            else:

                print("NRC=",response.value)

        else:

            print("NRC=",response.value)

    else:

        print("NRC=",response.value)

else:

    print("NRC=",response.value)
            
  