#include<stdio.h>
#include<string.h>
#include <conio.h>
#include <stdlib.h>

struct med {
    char name[100];
    int price;
    char description[100];
} drug_list[100] , tmp ;
char drug_list_name[20] = "drug_list.txt";

int drug_list_size = -1;
int cart[100][2];
int cart_size = 0;
int list_show_size = 5;

void list_of_drug ();
void show_drug(int start);

void buy_drug();
void show_cart(int start);

void add_to_cart();
void add_by_id(int id,int amount);

void remove_from_cart();
void remove_by_id(int id , int amount);
void fully_remove_item_in_cart(int id);

void clear_cart();

void check_out();
int total_price();

void exit_store();
void read_file();

int main (){

    read_file();
    char menu_input = '_'; // ตัวแปรสำหรับรับค่าใน menu
    while(menu_input != '0'){

        system("CLS");
        printf("*******************************\n\n");
        printf("WELLCOME TO LOCAL DRUGSTORE!!\n");
        printf("MENU..\n\n");
        printf("[0]EXIT\n");
        printf("[1]LIST OF DRUG\n");
        printf("[2]BUY DRUG\n");
        printf("\n*******************************\n");
        //scanf("%c",&menu_input);
        menu_input = getch();

        switch(menu_input){
            case '0' : // ออกจากโปรแกรม
                exit_store();
            break;

            case '1' : // ดูรายชื่อของยาทั้งหมด
                list_of_drug();
            break;

            case '2' : // จัดการซื้อยา
                buy_drug();
            break;
        }
    }
    return 0;
}

void list_of_drug (){ // ดูรายชื่อยา

    if(drug_list_size == -1){
        printf("Error! no drug list");
        exit(1);
    }else{
        char input = '_';
        int start = 0;
        while(input != '0'){
            system("CLS");
            printf("*******************************\n");
            printf("LIST OF DRUG\n");
            //printf("%d %d",start,drug_list_size);
            show_drug(start);
            printf("\n[0]MAIN MENU\n");
            printf("[<]PREVIOUS     [>]NEXT\n");
            printf("*******************************\n");

            input = getch();
            switch (input){
                case '.':
                case '>':

                    start += list_show_size;
                    if(start >= drug_list_size){
                        start -= list_show_size;
                    }
                break;
                case ',':
                case '<':
                    start -= list_show_size;
                    if(start < 0){
                        start = 0;
                    }
                break;
            }
        }
    }

}

void show_drug(int start){
    for(int i = start ; i < start+list_show_size ; i++){
        if ( i < drug_list_size ){
            printf("\n[%d] \n",i+1);
            printf("NAME        : %s \n",drug_list[i].name);
            printf("PRICE       : %d \n",drug_list[i].price);
            printf("DESCRIPTION : %s \n",drug_list[i].description);
        }
    }
}

void buy_drug(){ // ซื้อยา
    char input = '_';
    int start = 0;
    while(input != '0'){
        system("CLS");
        printf("*******************************\n");
        printf("BUY DRUG\n\n");
        printf("ITEM IN CART\n");
        show_cart(start);
        printf("\n");
        printf("[0]EXIT\n");
        printf("[1]ADD ITEM\n");
        printf("[2]REMOVE ITEM\n");
        printf("[3]CLEAR CART\n");
        printf("[4]CHECKOUT\n");
        printf("[<]PREVIOUS     [>]NEXT\n");
        printf("*******************************\n");
        input = getch();

        switch (input){
            case '1':
                add_to_cart();
            break;
            case '2':
                remove_from_cart();
            break;
            case '3':
                clear_cart();
            break;
            case '4':
                check_out();
            break;
            case '.':
            case '>':
                start += list_show_size;
                if(start >= cart_size){
                    start -= list_show_size;
                }
            break;
            case ',':
            case '<':
                start -= list_show_size;
                if(start < 0){
                    start = 0;
                }
            break;

        }
    }
}

void show_cart(int start){
    if(cart_size > 0){
        for( int i = start ; i < start + list_show_size ; i++ ){
            int show = cart[i][0];
                if( i < cart_size ){
                    printf("\n[%d]\n",i+1);
                    printf("NAME        : %s \n",drug_list[show].name);
                    printf("PRICE       : %d \n",drug_list[show].price);
                    printf("DESCRIPTION : %s \n",drug_list[show].description);
                    printf("AMOUNT      : %d \n",cart[i][1]);
                }
        }
    }else{
        printf("YOUR CART IS NOW EMPTY....\n");
    }
}

void add_to_cart(){
    int start = 0;
    int id_input = -1;
    int amount_input = 0;
    char input = '_';

    while(input != '0'){
        system("CLS");
        printf("*******************************\n");
        printf("ADD TO CART\n\n");
        printf("LIST OF DRUG\n");
        show_drug(start);
        printf("\n[0]BACK\n");
        printf("[1]ADD ITEM\n");
        printf("[<]PREVIOUS     [>]NEXT\n");
        printf("*******************************\n");
        input = getch();
        switch(input){
            case '1':
                printf("ENTER YOUR DRUG ID : ");
                scanf("%d",&id_input);
                if( 0 < id_input && id_input <= drug_list_size){
                printf("ENTER AMOUNT : ");
                scanf("%d",&amount_input);
                    if( amount_input > 0 ){
                        add_by_id(id_input-1,amount_input);
                    }else{
                        printf("AMOUT MUST EXCEED 0\n");
                        printf("PRESS ANY KEY TO CONTINUE...");
                        char _ ;
                        _ = getch();
                    }

                }else{
                    printf("DRUG NOT FOUND\n");
                    printf("PRESS ANY KEY TO CONTINUE...");
                    char _ ;
                    _ = getch();
                }
            break;
            case '.':
            case '>':
                start += list_show_size;
                if(start >= drug_list_size){
                    start -= list_show_size;
                }
            break;
            case ',':
            case '<':
                start -= list_show_size;
                if(start < 0){
                    start = 0;
                }
            break;

        }

    }
};

void add_by_id(int id,int amount){

    for( int i = 0 ; i < cart_size ; i++ ){
        if ( cart[i][0] == id){
            cart[i][1] += amount;
            return ;
        }
    }
    if( cart_size <= 100 ){
        cart[cart_size][0] = id;
        cart[cart_size][1] += amount;
        cart_size += 1;

    }else{
        printf("YOUR CART IS FULL\n");
        printf("PRESS ANY KEY TO CONTINUE...");
        char _ ;
        _ = getch();
    }

}

void remove_from_cart(){
    if ( cart_size == 0 ){
        printf("YOUR CART IS EMPTY\n");
        printf("PRESS ANY KEY TO CONTINUE...");
        char _ ;
        _ = getch();
        return ;
    }
    int start = 0;int total_price(){
    int total = 0;
    for(int i = 0 ; i < cart_size ; i++){
        int id = cart[i][0];
        total += ( drug_list[id].price * cart[i][1] );
    }
    return total;
};
    int id_input = -1;
    int amount_input = 0;
    char input = '_';

    while(input != '0'){
        system("CLS");
        printf("*******************************\n");
        printf("REMOVE ITEM\n\n");
        printf("ITEM IN CART\n");
        show_cart(start);
        printf("\n[0]BACK\n");
        printf("[1]REMOVE ITEM\n");
        printf("[<]PREVIOUS     [>]NEXT\n");
        printf("*******************************\n");
        input = getch();
        switch(input){
            case '1':
                printf("ENTER ITEM ID : ");
                scanf("%d",&id_input);
                printf("ENTER AMOUNT ,0 TO FULL REMOVE ITEM : ");
                scanf("%D",&amount_input);
                if ( 0 <= id_input && id_input <= cart_size){
                    remove_by_id(id_input-1,amount_input);
                }else{
                    printf("ITEM NOT FOUND\n");
                    printf("PRESS ANY KEY TO CONTINUE...");
                    char _ ;
                    _ = getch();
                }
            break;
            case '.':
            case '>':
                start += list_show_size;
                if(start >= drug_list_size){
                    start -= list_show_size;
                }
            break;
            case ',':
            case '<':
                start -= list_show_size;
                if(start < 0){
                    start = 0;
                }
            break;
        }
    }


};

void remove_by_id(int id , int amount){
    if (amount <= 0){
        fully_remove_item_in_cart(id);
        return ;
    }
    cart[id][1] -= amount;
    if( cart[id][1] <= 0 ){
        fully_remove_item_in_cart(id);
    }

};

void fully_remove_item_in_cart(int id){

    if( cart_size == 1){
        cart[0][0] = -1;
        cart[0][1] = 0;
        cart_size = 0;
        return ;
    }
    cart_size -= 1;
    for(int i = id ; i < cart_size ; i++){
        cart[i][0] = cart[i+1][0];
        cart[i][1] = cart[i+1][1];
    }

};

void clear_cart(){
    if ( cart_size == 0 ){
        printf("YOUR CART IS EMPTY\n");
        printf("PRESS ANY KEY TO CONTINUE...");
        char _ ;
        _ = getch();
        return ;
    }

    for(int i = 0 ; i < cart_size ; i++){
        cart[i][0] = -1;
        cart[i][1] = 0;
    }
    cart_size = 0;
};

void check_out(){
    if ( cart_size == 0 ){
        printf("YOUR CART IS EMPTY\n");
        printf("PRESS ANY KEY TO CONTINUE...");
        char _ ;
        _ = getch();
        return ;
    }
    char input = '_';
    while(input != '0'){
        system("CLS");
        printf("*******************************\n");
        printf("CHECK OUT\n\n");
        printf("ITEM IN CART\n\n");
        int total = total_price();
        printf("\nAMOUNT = %d\n",total);
        printf("\n[0]BACK\n");
        printf("[1]CHECKOUT ITEM\n");
        printf("*******************************\n");
        input = getch();
        if(input == '1'){
            int paid ;
            printf("ENTER PAY AMOUNT : ");
            scanf("%d",&paid);
            int change = paid - total;
            if ( change >= 0 ){
                printf("CHANGE : %d BAHT\n",change);
                clear_cart();

            }else{
                printf("MONEY IS NOT NOUGHT TO PURCHSE\n");
            }
            printf("PRESS ANY KEY TO CONTINUE...");
            char _ ;
            _ = getch();
            return ;
        }
    }


};

int total_price(){
    int total = 0;
    for(int i = 0 ; i < cart_size ; i++){
        int id = cart[i][0];
        int total_per_drug = ( drug_list[id].price * cart[i][1] );
        printf("%s : %d * %d = %d\n",drug_list[id].name,drug_list[id].price,cart[i][1],total_per_drug);
        total += total_per_drug;
    }
    return total;
};

void exit_store(){ // ออกจากร้าน
    system("CLS");
    printf("*******************************\n\n");
    printf("THANKS YOU\n");
    printf("\n*******************************\n");
};

void read_file(){ // อ่านไฟล์มาเก็บไว้ใน array

    FILE *fptr;
    if ((fptr = fopen(drug_list_name,"r")) == NULL){
       printf("Error! opening file");
       exit(1);
    }

    char tmp_name[100];
    int tmp_price;
    char tmp_description[100];
    fscanf(fptr,"%d", &drug_list_size);
    for(int i = 0 ; i < drug_list_size ; i++){
        fscanf(fptr,"%s", &tmp_name);
        fscanf(fptr,"%d", &tmp_price);
        fscanf(fptr,"%s", &tmp_description);
        //printf("%s %d %s \n",tmp_name,tmp_price,tmp_description);
        strcpy(drug_list[i].name ,tmp_name);
        drug_list[i].price = tmp_price;
        strcpy(drug_list[i].description ,tmp_description);
    }
    fclose(fptr);

}
