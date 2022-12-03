
def lms_engine(p_logger,p_md, p_cust_name, p_cust_cs, p_cust_loan_amt):
    p_logger.info('Caluculating LMS Data for customer:+p_cust_name')
    result = {}
    for lkp in p_md:
        # print(lkp)
        if p_cust_cs >=lkp["cs_start"] and p_cust_cs<=lkp["cs_end"] and p_cust_loan_amt >=lkp["loan_amt_start"] and p_cust_loan_amt<=lkp["loan_amt_end"]:
            # print(lkp["interest"])
            # print(lkp["duration"])
            total_amt = p_cust_loan_amt + (p_cust_loan_amt * (lkp["interest"]/100))
            print(p_cust_name,"Your Loan is approved, details:")
            print('Principal',str(p_cust_loan_amt))
            print('Interest Amt',str((p_cust_loan_amt * (lkp["interest"]/100))))
            print('total',str(total_amt))

            p_logger.info(p_cust_name + "Your Loan is approved, details:")
            p_logger.info('Principal' + str(p_cust_loan_amt))
            p_logger.info('Interest Amt' + str((p_cust_loan_amt * (lkp["interest"]/100))))
            p_logger.info('total' + str(total_amt))


           
            result["Message"] = p_cust_name + " Your Loan is approved, details:"
            result["Principal"] = p_cust_loan_amt
            result["Interest"] = p_cust_loan_amt * (lkp["interest"]/100)
            result["Total"] = total_amt
            break
    return result