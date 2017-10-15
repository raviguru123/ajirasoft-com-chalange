def max(num1,num2):
    if(num1>num2):
        return num1;
    return num2;

def Longest_Common_Subsequence(str1,str2):
      m=len(str1);
      n=len(str2);
      output=[[None]*(n+1) for i in range(m+1)];

      for i in range(m+1):
          for j in range(n+1):
                if(i==0 or j==0):
                    output[i][j]=0;
                elif(str1[i-1]==str2[j-1]):
                    output[i][j]=output[i-1][j-1]+1;
                else:
                    output[i][j]=max(output[i-1][j],output[i][j-1]);
         
      return output[m][n];

def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        arr_size=list(map(int,input().split()));
        arr1=list(input());
        arr2=list(input());
        output.append(Longest_Common_Subsequence(arr1,arr2));
           
    for i in output:
        print(i);

if(__name__=='__main__'):
    main();


