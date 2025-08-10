#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main(void){
    /*printing ****
               ****
               ****
    */
    int rows;
    cout << "Enter rows:  " << endl;
    cin >> rows;
    for(int i = 0; i< rows; i++){
        for(int j=0; j < rows; j++){
            cout << "*" ;
        }
        cout<<"\n";
    }
    /*printing: *
                **
                ***
                ****
    */
    cout<<"\n\n\n\n\n";
    for(int a= 0; a < rows; a++){
        for(int b = 0 ; b<=a; b++){
            cout<<"*";
        }
        cout<<endl;
    }
    /*printing: 1
                1 2
                1 2 3
                1 2 3 4
    */
    cout<<"\n\n\n\n\n";
    for (int i = 0; i<rows; i++){
        for (int j = 1; j<=i;j++){
            cout<<j << " ";
        }
        cout<<endl;
    }
    /* printing : 1
                  2 2
                  3 3 3
                  4 4 4 4
    */
    cout<<"\n\n\n\n\n";
    for(int a= 1; a<=rows; a++){
        for(int b = 0; b<a; b++){
            cout<< a << " ";
        }
        cout << endl;
    }
    /* printing: 5 5 5 5 5
                 4 4 4 4
                 3 3 3
                 2 2
                 1
    */
    cout<<"\n\n\n\n\n";
    for(int i = 0; i < rows; i++){
        // rows-i times print for each iteration
        for(int j = 1; j<= rows-i ; j++){
            cout<<j<< " ";
        }
        cout<<endl;
    }
    /*printing: *
               ***
              *****
             *******
    */
    cout<<"\n\n\n\n\n";
    for(int i = 1; i<=rows;i++){
        // follows 2 * rows - 1 logic for number of stars on each row
        // another loop for space?
        for(int y = 0; y <= rows - i ; y++){
            cout<< " ";
        }
        for(int j = 1; j<= (2*i) - 1 ; j++){
            cout<<"*";
        }        
        cout<<endl;
    }
    /*printing: *******
                 *****
                  ***
                   *
    */
    cout<<"\n\n\n\n\n";
    for(int i = 0; i < rows; i++){
        for(int y= rows; y> rows-i ; y--){
            cout<< " ";
        }   
        //this time each row has exactly row - i *2 - 1  
        for(int j = 0; j<(2*(rows-i))-1;j++ ){
            cout<<"*";
        }
        cout<<endl;
    }
    
    cout<<"\n\n\n\n\n";
    for(int i = 1; i<=rows;i++){
        // follows 2 * rows - 1 logic for number of stars on each row
        // another loop for space?
        for(int y = 0; y <= rows - i ; y++){
            cout<< " ";
        }
        for(int j = 1; j<= (2*i) - 1 ; j++){
            cout<<"*";
        }        
        cout<<endl;
    }
    for(int i = 0; i < rows; i++){
        for(int y= rows; y>= rows-i ; y--){
            cout<< " ";
        }   
        //this time each row has exactly row - i *2 - 1  
        for(int j = 0; j<(2*(rows-i))-1;j++ ){
            cout<<"*";
        }
        cout<<endl;
    }
    /*combining some more patterns: */
    cout<<"\n\n\n\n\n";
    for(int a= 0; a < rows; a++){
        for(int b = 0 ; b<=a; b++){
            cout<<"*";
        }
        cout<<endl;
    }
    for(int a = 1; a<rows; a++){
        //each row has rows-i *
        for(int j = 1 ; j<= rows-a ; j++){
            cout<<"*";
        }
        cout<<endl;
    }
    /*printing 1 0 pattern*/
    cout<< "\n\n\n\n\n";
    for(int i = 1; i<= rows; i++){
        for(int j=1; j<=i; j++){
            if(i%2 == 0){
                if(j%2 == 0){
                    cout<< " 1 ";
                }
                else{
                    cout<< " 0 ";
                }
            }
            else{
                if(j%2 == 0){
                    cout<<" 0 ";
                }
                else{
                    cout<<" 1 ";
                }

            }
            

        }
        cout<< endl;
    }
    /*pattern for twin - towers like structure*/
    cout<<"\n\n\n\n\n";
    for(int i = 0; i<rows; i++){
        for(int j = 0; j<=i; j++){
            cout<<j+1;
        }
        for(int space = 0; space < ((rows-i)*2) - 2; space++){
            cout<<" ";
        }
        for(int k = i; k>=0; k--){
            cout<<k+1;
        }
        cout<<endl;
    }
    /*more patterns:- */
    cout<<"\n\n\n\n\n";
    for(int i = 0; i<rows; i++){
        for(int j = 0; j<=i; j++){
            cout<<"*";
        }
        for(int space = 0; space < ((rows-i)*2) - 2; space++){
            cout<<" ";
        }
        for(int k = i; k>=0; k--){
            cout<<"*";
        }
        cout<<endl;
    }
    for(int i = 1; i<rows;i++){
        for(int j = rows-1; j>= i; j--){
            cout<<"*";
        }
        for(int space = 0 ; space < i*2  ;space++ ){
            cout<<" ";
        }
        for(int k = rows-1; k>=i; k--){
            cout<<"*";
        }
        cout<<endl;
    }
}