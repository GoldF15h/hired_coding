#include<stdio.h>
#include<string.h>
#include<conio.h>
#include<stdlib.h>

#define _CRT_SECURE_NO_WARNINGS

struct med {
    char name[100];
    int price;
} drug_list[100] , tmp ;
char drug_list_name[20] = "drug_list.txt";

char _ ;
int drug_list_size = -1;
int cart[100][2];
int cart_size = 0;

void list_of_drug ();
void show_drug();

void buy_drug();
void show_cart();

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
int search_drug();

int main (){

	char menu_input = '_';
    read_file();

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
        menu_input = _getch();

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

	char input = '_';
    int start = 0,id;
    if(drug_list_size == -1){
        printf("Error! no drug list");
        exit(1);
    }else{
        input = '_';
        start = 0;
        while(input != '0'){
            system("CLS");
            printf("*******************************\n");
            printf("LIST OF DRUG\n");
            //printf("%d %d",start,drug_list_size);
            show_drug(start);
            printf("\n[0]MAIN MENU\n");
            printf("[1]DRUG SEARCH\n");
            printf("*******************************\n");

            input = _getch();
            switch (input){
                case '1':
                    id = search_drug();
                    printf("\n");
                    if ( id >= 0 ){
                        printf("DRUG FOUND!!\n");
                        printf("\n[%d] \n",id+1);
                        printf("NAME        : %s \n",drug_list[id].name);
                        printf("PRICE       : %d \n",drug_list[id].price);
                    }
                    else{
                        printf("DRUG NOT FOUND!!\n");
                    }
                    printf("\nPRESS ANY KEY TO CONTINUE...");
                    _ = _getch();
                break;

            }
        }
    }

}

void show_drug(){
	int i;
    for(i = 0 ; i < drug_list_size ; i++){
        printf("\n[%d] \n",i+1);
        printf("NAME        : %s \n",drug_list[i].name);
        printf("PRICE       : %d \n",drug_list[i].price);
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
        printf("*******************************\n");
        input = _getch();

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
        }
    }
}

void show_cart(){
	int i;
	int show;
    if(cart_size > 0){
        for( i = 0 ; i < cart_size ; i++ ){
            show = cart[i][0];
            printf("\n[%d]\n",i+1);
            printf("NAME        : %s \n",drug_list[show].name);
            printf("PRICE       : %d \n",drug_list[show].price);
            printf("AMOUNT      : %d \n",cart[i][1]);

        }
    }else{
        printf("YOUR CART IS NOW EMPTY....\n");
    }
}

void add_to_cart(){
    int start = 0;
    int amount_input = 0;
    int id = -1;
    char input = '_';
    char add_input = '_';

    while(input != '0'){
        system("CLS");
        printf("*******************************\n");
        printf("ADD TO CART\n\n");
        printf("LIST OF DRUG\n");
        show_drug(start);
        printf("\n[0]BACK\n");
        printf("[1]ADD ITEM\n");
        printf("[2]SEARCH FOR DRUG\n");
        printf("*******************************\n");
        input = _getch();
        switch(input){
            case '1':
                printf("ENTER YOUR DRUG ID : ");
                scanf("%d",&id);
                if( id >= 0 ){
                    printf("\n[%d]\n",id+1);
                    printf("NAME        : %s \n",drug_list[id].name);
                    printf("PRICE       : %d \n",drug_list[id].price);
                    printf("IS THAT WHAT YOU WANT TO ADD? [Y/N]\n");
                    while( add_input != 'y' && add_input != 'Y'  && add_input != 'n'  && add_input != 'N'  ){
                        add_input = _getch();
                        if(add_input == 'y' || add_input == 'Y'){
                            printf("ENTER AMOUNT : ");
                            scanf("%d",&amount_input);
                            if( amount_input > 0 ){
                                add_by_id(id,amount_input);
                            }else{
                                printf("AMOUT MUST EXCEED 0\n");
                                printf("PRESS ANY KEY TO CONTINUE...");
                                _ = _getch();
                            }
                        }
                    }
                    add_input = '_';
                }else{
                    printf("DRUG NOT FOUND 0\n");
                    printf("PRESS ANY KEY TO CONTINUE...");
                    _ = _getch();

                }

            break;
            case '2':
                id = search_drug();
                if( id >= 0 ){
                    printf("\n[%d]\n",id+1);
                    printf("NAME        : %s \n",drug_list[id].name);
                    printf("PRICE       : %d \n",drug_list[id].price);
                    printf("IS THAT WHAT YOU WANT TO ADD? [Y/N]\n");
                    while( add_input != 'y' && add_input != 'Y'  && add_input != 'n'  && add_input != 'N'  ){
                        add_input = _getch();
                        if(add_input == 'y' || add_input == 'Y'){
                            printf("ENTER AMOUNT : ");
                            scanf("%d",&amount_input);
                            if( amount_input > 0 ){
                                add_by_id(id,amount_input);
                            }else{
                                printf("AMOUT MUST EXCEED 0\n");
                                printf("PRESS ANY KEY TO CONTINUE...");
                                _ = _getch();
                            }
                        }
                    }
                    add_input = '_';
                }else{
                    printf("DRUG NOT FOUND 0\n");
                    printf("PRESS ANY KEY TO CONTINUE...");
                    _ = _getch();

                }
            break;
        }

    }
};

void add_by_id(int id,int amount){

	int i;
    for( i = 0 ; i < cart_size ; i++ ){
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

        _ = _getch();
    }

}

void remove_from_cart(){
	int start = 0;
    int id_input = -1;
    int amount_input = 0;
    char input = '_';
    if ( cart_size == 0 ){
        printf("YOUR CART IS EMPTY\n");
        printf("PRESS ANY KEY TO CONTINUE...");

        _ = _getch();
        return ;
    }
    while(input != '0'){
        system("CLS");
        printf("*******************************\n");
        printf("REMOVE ITEM\n\n");
        printf("ITEM IN CART\n");
        show_cart(start);
        printf("\n[0]BACK\n");
        printf("[1]REMOVE ITEM\n");
        printf("*******************************\n");
        input = _getch();
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

                    _ = _getch();
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

	int i;
    if( cart_size == 1){
        cart[0][0] = -1;
        cart[0][1] = 0;
        cart_size = 0;
        return ;
    }
    cart_size -= 1;
    for(i = id ; i < cart_size ; i++){
        cart[i][0] = cart[i+1][0];
        cart[i][1] = cart[i+1][1];
    }

};

void clear_cart(){
	int i;
    if ( cart_size == 0 ){
        printf("YOUR CART IS EMPTY\n");
        printf("PRESS ANY KEY TO CONTINUE...");
        _ = _getch();
        return ;
    }

    for(i = 0 ; i < cart_size ; i++){
        cart[i][0] = -1;
        cart[i][1] = 0;
    }
    cart_size = 0;
};

void check_out(){
	char input = '_';
	int total;
	int paid ;
	int change;
    if ( cart_size == 0 ){
        printf("YOUR CART IS EMPTY\n");
        printf("PRESS ANY KEY TO CONTINUE...");
        _ = _getch();
        return ;
    }
    while(input != '0'){
        system("CLS");
        printf("*******************************\n");
        printf("CHECK OUT\n\n");
        printf("ITEM IN CART\n\n");
        total = total_price();
        printf("\nAMOUNT = %d\n",total);
        printf("\n[0]BACK\n");
        printf("*******************************\n");
        input = _getch();
    }
};

int total_price(){
    int total = 0;
	int i,id,total_per_drug;
    for(i = 0 ; i < cart_size ; i++){
        id = cart[i][0];
        total_per_drug = ( drug_list[id].price * cart[i][1] );
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

	char tmp_name[100];
    int tmp_price;
    char tmp_description[100];
	int i;
    FILE *fptr;

	fptr = fopen("drug_list.txt","r");
    if (fptr == NULL){
       printf("Error! opening file");
	   _ = _getch();
       exit(1);
    }
    fscanf(fptr,"%d", &drug_list_size);
    for(i = 0 ; i < drug_list_size ; i++){
        fscanf(fptr,"%s", &tmp_name);
        fscanf(fptr,"%d", &tmp_price);
        //printf("%s %d %s \n",tmp_name,tmp_price,tmp_description);
        strcpy(drug_list[i].name ,tmp_name);
        drug_list[i].price = tmp_price;
    }
    fclose(fptr);

}

int search_drug(){
    char search[100];
    int i,j,len,slen;
    printf("TPYE WHAT YOU WANT TO SEARCH : ");
    scanf("%s",&search);
    len = strlen(search);
    for(i = 0 ; i < drug_list_size ; i++){
        slen = strlen(drug_list[i].name);
        if( len <= slen ){
            j = 0;
            while( j < len ){
            if( drug_list[i].name[j] != search[j] ){
                break;
            }
            j++;
        }
        if ( j == len )
            return i;
        }
    }
    return -1;
};
