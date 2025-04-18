classification_prompt="""You are an expert in Natural Language Processing and Question Classification. Your task is to classify a given sentence into  the following five categories.A given
  query can belong to more than 1 class.Return only the classes that the respective sentence could possibly belong to,don't bother with an explanation.Each and every
  single statement has to be classified.

  To classify a question as Factual, check if:
1. The answer is a straightforward, singular piece of information
2. The response can be verified through standard reference sources
3. No complex reasoning or multiple steps are needed to answer
4. The question asks "What", "Who", "When", "Where" with a specific focus
Example: ->How much did HPE return to shareholders in Q3 2024 through dividends and share repurchases?
         ->What was HPE’s operating profit margin for the Hybrid Cloud segment in Q4 2024?
         ->When was the dividend for Q4 2024 scheduled to be paid?
         ->How much was HPE’s Financial Services segment’s net portfolio assets in Q4 2024?

To classify a question as Aggregate/Time-based, verify if:
1. The question requires data collection over a specific time period
2. The answer involves statistical aggregation or trend analysis
3. Numerical summation or average calculation is central to the response
4. The timeframe is explicitly defined or implied
Example:  ->What was the highest recorded revenue for any quarter in fiscal year 2024?
          ->How has HPE’s ARR changed from Q1 2023 to Q4 2024?
          ->Compare HPE’s Intelligent Edge operating margins over the last four quarters.
          ->Which quarter in fiscal year 2024 had the highest operating profit margin for the Server segment?
          ->Track the changes in Hybrid Cloud revenue from Q1 2023 to Q4 2024.

To classify a question as Global Sensing, ensure:
1. The question requires understanding complex global interactions
2. Multiple perspectives and contextual analysis are necessary
3. The response involves systemic thinking beyond local boundaries
4. Interdisciplinary knowledge is required to provide a comprehensive answer
Example:   ->Summarize the revenue trends and executive statements for all quarters in 2024.
           ->How did the Juniper Networks acquisition impact HPE’s 2024 outlook?
           ->What major financial milestones did HPE achieve in fiscal year 2024?
           ->Provide a breakdown of HPE’s profitability in 2024.
           ->What were the biggest financial takeaways from HPE’s earnings reports in 2024?

To classify a question as Reasoning/Inference, check if:
1. The question requires extrapolating beyond existing information
2. Logical deduction and predictive analysis are central
3. Multiple potential scenarios or outcomes must be considered
4. The answer involves explaining probable consequences or mechanisms
Example:   ->Based on past trends, which segment is likely to experience the highest revenue growth in 2025?
           ->What factors contributed to HPE’s decline in gross margins throughout 2024?
           ->How might the Juniper Networks acquisition influence HPE’s networking revenue in 2025?
           ->Why did HPE increase its full-year EPS guidance in Q3 2024?

To classify a question as Multi-Part, verify:
1. The question contains multiple distinct but interconnected components
2. A comprehensive response requires exploring various dimensions
3. Simple, linear answers are insufficient
4. Synthesis and integration of different perspectives are necessary
Example:   ->When was HPE's ARR $1.7 billion, and what was the free cash flow that year?
           ->What were HPE's revenue and net earnings per share (EPS) in Q3 2024, and how did they compare to Q2 2024?
           ->List the operating profit margins for all business segments in Q4 2024 and their percentage change from the prior year.
           ->How did HPE’s Intelligent Edge segment perform in Q1 and Q4 2024, and what factors contributed to the change.
Return only the relevant class, no explanation needed.
  """