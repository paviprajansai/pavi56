{ 
    // Calling order function 
    int n = order(x); 
    int temp = x, sum = 0; 
    while (temp) 
    { 
        int r = temp%10; 
        sum += power(r, n); 
        temp = temp/10; 
    } 
  
    // If satisfies Armstrong condition 
    return (sum == x); 
} 
  
// Driver Program 
int main() 
{ 
    int x = 153; 
    cout << isArmstrong(x) << endl; 
    x = 1253; 
    cout << isArmstrong(x) << endl; 
    return 0; 
} 
