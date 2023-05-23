--Oracle dynamic SQL statements example using EXECUTE IMMEDIATE


PROCEDURE P_SALE_RPT
IS
    v_old_CON_ID HR.TAB_SALE_CONTRACT.CONTRACT_ID%TYPE DEFAULT 0; --rec loop CONTRACT_ID change to next row
    v_update_cnt PLS_INTEGER DEFAULT 0;
    
BEGIN
    DELETE FROM HR.taw_sale_rpt;
    COMMIT;
    
    FOR rec in (
               SELECT r.CONTRACT_ID,cont.CONTRACT_NO,
                      cust.CUST_NAME,cust.CUST_INFO ,
                      r.RECVTERM_ID,r.receivable_AMT,r.received_AMT 
               FROM HR.TAB_SALE_CONTRACT cont, HR.TAB_SALE_CUST cust,HR.TAB_SALE_RECEIVABLE r 
               WHERE r.CONTRACT_ID = cont.CONTRACT_ID
               and   cont.cust_id = cust.cust_id
               order by  r.CONTRACT_ID,r.RECVTERM_ID 
            )
    LOOP
        --IS new contract 
        IF v_old_CON_ID <> rec.CONTRACT_ID THEN 
            --New contract, insert
            INSERT INTO taw_sale_rpt (contract_id, contract_no,cust_name, cust_info, 
                                        A0000_receivable_amt,A0000_received_amt,
                                        total_receivable_AMT,total_received_AMT)
                VALUES (rec.contract_id, rec.contract_no,rec.cust_name, rec.cust_info,
                                        rec.receivable_AMT,rec.received_AMT,
                                        rec.receivable_AMT,rec.received_AMT);
        ELSE
            --Same contract,update 
            /*
            UPDATE taw_sale_rpt
            SET A0001_receivable_AMT = rec.receivable_AMT,
                A0001_received_AMT = rec.received_AMT,
                total_receivable_AMT = total_receivable_AMT + rec.receivable_AMT,
                total_received_AMT = total_received_AMT + rec.received_AMT
            WHERE CONTRACT_ID = rec.contract_id;
            
            UPDATE taw_sale_rpt
            SET A0002_receivable_AMT = rec.receivable_AMT,
                A0002_received_AMT = rec.received_AMT,
                total_receivable_AMT = total_receivable_AMT + rec.receivable_AMT,
                total_received_AMT = total_received_AMT + rec.received_AMT
            WHERE CONTRACT_ID = rec.contract_id;
            
            ...and so on
            */
           
             
             EXECUTE IMMEDIATE
                'UPDATE TAW_SALE_RPT SET '||
                rec.RECVTERM_ID||'_receivable_amt = :amt_1,'||
                rec.RECVTERM_ID||'_received_amt = :amt_2,'||
                'total_receivable_AMT = total_receivable_AMT + :amt_3,'||
                'total_received_AMT = total_received_AMT + :amt_4 '||
                'WHERE CONTRACT_ID = :con_id'
             USING rec.receivable_AMT, rec.received_AMT,rec.receivable_AMT, rec.received_AMT,rec.contract_id;

             
             
             v_update_cnt := SQL%ROWCOUNT;
             IF v_update_cnt <> 1 THEN
                 DBMS_OUTPUT.put_line ('CONTRACT='||rec.contract_id||'R_ID='||rec.RECVTERM_ID||'NUM='||v_update_cnt);              
             END IF;
             
             
        END IF; 
        
            
        v_old_CON_ID := rec.CONTRACT_ID; 
        COMMIT;
    END LOOP; 
    
    DBMS_OUTPUT.put_line ('OK!'); 
    
    EXCEPTION
      WHEN OTHERS THEN
        DBMS_OUTPUT.put_line ('Error in P_SALE_RPT:'||SqlErrm);
        RAISE; 
end P_SALE_RPT; 
