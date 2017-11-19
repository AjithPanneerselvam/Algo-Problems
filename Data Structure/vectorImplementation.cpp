#include<iostream>
#include<stdlib>
using namespace std;

class vector{
  int size_;
  int* array_;
  int index_;

public:
  vector(int size = 0){
    size_ = size;
    array_ = new[size];
  }



  ~vector(){

  }


};
