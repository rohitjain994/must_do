int uneatenusingNaive(int N, vector<int> A)
{
    int eaten = 0;
    vector<bool>seen(N+1, false);
    for (int i = 0; i < A.size(); i++)
    {
        long Ai = A[i];
        long j = A[i];
        while (j <= N && j>0)
        {
            if (!seen[j])
            {
                seen[j] = true;
                eaten++;
            }
            j += Ai;
        }
    }
    return N - eaten;
}


long result = 0;

for(int i = 1; i < 1 << K; i++){
     long lcm = 1;
     for(int j = 0; j < K; j++)
        if(((1<<j) & i) != 0) //if bit j is set, compute new LCM after including A[j]
           lcm *= A[j]/gcd(lcm, A[j]);
     if(number of bit set in i is odd)
        result += N/lcm;
     else
        result -= N/lcm; 
}