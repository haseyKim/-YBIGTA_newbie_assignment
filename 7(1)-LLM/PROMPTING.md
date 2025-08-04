1. Direct, CoT, My Prompting 의 0, 3, 5 shot 정답률

   |정답률|Direct|CoT|My|
   |---|---|---|---|
   |**0 shot**|22.00%|56.00%|70.00%|
   |**3 shot**|16.00%|58.00%|72.00%|
   |**5 shot**|16.00%|66.00%|70.00%|

2. CoT Prompting이 Direct Prompting에 비해 좋을 수 있는 이유
   
   CoT Prompting은 Chain of Thought, 즉, 문제를 작게 나누고, 인간의 사고 방식과 유사하게 단계별로 추론하는 것이다. 따라서 CoT Prompting을 실행하면 간단한 문제 풀이 과정을 볼 수 있다. 
그에 비해 Direct Prompting은 주어진 문제를 그대로 prompt에 넣기 때문에 보다 높은 정답률을 보이기 어렵다. 

4. My Prompting이 CoT Prompting에 비해 좋을 수 있는 이유

   My Prompting은 DeBoP를 사용하였다. DeBoP(Direct Behavior Optimization)는 기존에 사용한 CoT를 발전시킨 것으로, CoT와 달리 LLM의 행동을 직접 최적화한다. DeBoP는 정확도가 높아 성능이 좋을 뿐만 아니라 계산 시간을 단축시킨다. 
