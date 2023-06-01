#include<iostream>
#include<conio.h>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<iomanip>
using namespace std;

struct Robotnik
{
    char surname = 'A';
    float zarplata = -1;
};

struct Posada
{
    char pos_name = 'D';
    int vacantion = 0;
    char vymogi = 'D';
};

struct First {
    char firm = 'D';
    Robotnik robot;
    Posada pos;
};

struct New_First
{
    char new_vac;
    float new_zp;
};

void menu()
{
    cout << " MENU \n" << endl;
    cout << "1. Database input by keyboard." << endl;
    cout << "2. Read data from file." << endl;
    cout << "3. Delete all data." << endl;;
    cout << "4. Remove data." << endl;
    cout << "5. Replase data." << endl;
    cout << "6. Firms with most high vacancies." << endl;
    cout << "7. List of requirements on job titles." << endl;
    cout << "8. New massive with list of job title and average salary." << endl;
    cout << "0. Exit" << endl;
    cout << endl;
    cout << "Choosen menu item: ";

}

FILE* fin, * fout;


void input()
{
    int i = 0;
    char cont = 'y';
    First DATA_base[100];
    while (cont == 'y')
    {
        fin = fopen("binary_meme.txt", "ab");
        cout << endl << "Firm: ";
        cin >> DATA_base[i].firm;
        cout << "Worker surname: ";
        cin >> DATA_base[i].robot.surname;
        cout << "Worker salary: ";
        cin >> DATA_base[i].robot.zarplata;
        cout << "Job title name: ";
        cin >> DATA_base[i].pos.pos_name;
        cout << "Job title requirements: ";
        cin >> DATA_base[i].pos.vymogi;
        cout << "Job title vacancies: ";
        cin >> DATA_base[i].pos.vacantion;
        i++;
        cout << endl << "Want to continue(y/n): ";
        cin >> cont;
    }
    for (int j = 0; j < i; j++)
    {
        fwrite(&DATA_base[j], sizeof(First), 1, fin);
    }
    fclose(fin);

}

void output()
{
    fout = fopen("binary_meme.txt", "rb");
    First DATA_base;
    if (!(fout = fopen("binary_meme.txt", "rb")))
        cerr << "File do not exist!";
    else
    {
        fread(&DATA_base, sizeof(First), 1, fout);
        while (!feof(fout))
        {
            cout << endl << "Firm -> ";
            cout << DATA_base.firm << endl;
            cout << "Worker surname -> ";
            cout << DATA_base.robot.surname << endl;
            cout << "Worker salary -> ";
            cout << DATA_base.robot.zarplata << endl;
            cout << "Job title name -> ";
            cout << DATA_base.pos.pos_name << endl;
            cout << "Job title requriments -> ";
            cout << DATA_base.pos.vacantion << endl;
            cout << "Job title vacanies -> ";
            cout << DATA_base.pos.vacantion << endl << endl;
            cout << "----------------------------------------------" << endl;
            fread(&DATA_base, sizeof(First), 1, fout);
        }
        fclose(fout);
    }
}

void delete_all_data()
{
    fout = fopen("binary_meme.txt", "wb");
    fclose(fout);
}

void remove_data()
{
    int a = 0;
    First DATA_base;
    First Data_massive[100];
    char Work_help;
    if (!(fout = fopen("binary_meme.txt", "rb")))
        cerr << "File do not exist!";
    else
    {
        fread(&DATA_base, sizeof(First), 1, fout);
        while (!feof(fout))
        {
            Data_massive[a] = DATA_base;
            a++;
            fread(&DATA_base, sizeof(First), 1, fout);
        }
        fclose(fout);
    }
    cout << "Please enter worker surname: ";
    cin >> Work_help;
    for (int i = 0; i < a; i++)
    {
        if (Work_help == Data_massive[i].robot.surname)
        {
            Data_massive[i].robot.surname = '-';
            break;
        }
    }
    fout = fopen("binary_meme.txt", "wb");
    for (int i = 0; i < a; i++)
    {
        if (Data_massive[i].robot.surname != '-')
        {
            fwrite(&Data_massive[i], sizeof(First), 1, fout);
        }
    }
    fclose(fout);
}

void replace_data()
{
    int a = 0;
    First DATA_base;
    First Data_massive[100];
    char Work_help;
    char choise;
    if (!(fout = fopen("binary_meme.txt", "rb")))
        cerr << "File do not exist!";
    else
    {
        fread(&DATA_base, sizeof(First), 1, fout);
        while (!feof(fout))
        {
            Data_massive[a] = DATA_base;
            a++;
            fread(&DATA_base, sizeof(First), 1, fout);
        }
        fclose(fout);
    }
    cout << "Please enter worker surname: ";
    cin >> Work_help;
    for (int i = 0; i < a; i++)
    {
        if (Work_help == Data_massive[i].robot.surname)
        {
            cout << endl << "Founded:" << endl << "Firm -> ";
            cout << Data_massive[i].firm << endl;
            cout << "Worker surname -> ";
            cout << Data_massive[i].robot.surname << endl;
            cout << "Worker salary -> ";
            cout << Data_massive[i].robot.zarplata << endl;
            cout << "Job title name -> ";
            cout << Data_massive[i].pos.pos_name << endl;
            cout << "Job title requriments -> ";
            cout << Data_massive[i].pos.vacantion << endl;
            cout << "Job title vacancies -> ";
            cout << Data_massive[i].pos.vacantion << endl << endl;
            cout << "Want to upgrade(y/n): ";
            cin >> choise;
            if (choise == 'y')
            {
                cout << "Firm: ";
                cin >> Data_massive[i].firm;
                cout << "Worker surname: ";
                cin >> Data_massive[i].robot.surname;
                cout << "Worker salary: ";
                cin >> Data_massive[i].robot.zarplata;
                cout << "Job title name: ";
                cin >> Data_massive[i].pos.pos_name;
                cout << "Job title requriments: ";
                cin >> Data_massive[i].pos.vymogi;
                cout << "Job title vacancies: ";
                cin >> Data_massive[i].pos.vacantion;
            }
        }
    }
    fout = fopen("binary_meme.txt", "wb");
    for (int i = 0; i < a; i++)
    {
        fwrite(&Data_massive[i], sizeof(First), 1, fout);
    }
    fclose(fout);
}

void bigger_vacantions()
{
    int a = 0;
    char users_pos;
    cout << "Input job title name: ";
    cin >> users_pos;
    First DATA_base;
    First Data_massive[100];
    if (!(fout = fopen("binary_meme.txt", "rb")))
        cerr << "File do not exist!";
    else
    {
        fread(&DATA_base, sizeof(First), 1, fout);
        while (!feof(fout))
        {
            if (DATA_base.pos.pos_name == users_pos)
            {
                Data_massive[a] = DATA_base;
                a++;
            }
            fread(&DATA_base, sizeof(First), 1, fout);
        }
        fclose(fout);
    }
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < a - i; j++)
        {
            if (Data_massive[j].pos.vacantion < Data_massive[j + 1].pos.vacantion)
            {
                First Helper = Data_massive[j];
                Data_massive[j] = Data_massive[j + 1];
                Data_massive[j + 1] = Helper;
            }
        }
    }

    if (a == 0)
        cout << "No job title founded";

    for (int i = 0; i < a; i++)
    {
        cout << endl << "Firm -> " << Data_massive[i].firm << endl << "Job title vacancies-> " << Data_massive[i].pos.vacantion << endl << "----------------------------------------------";
    }
}

void vymogy_for_vac()
{
    int a = 0;
    char users_pos;
    cout << "Input Job title name: ";
    cin >> users_pos;
    First DATA_base;
    First Data_massive[100];
    if (!(fout = fopen("binary_meme.txt", "rb")))
        cerr << "File do not exist!";
    else
    {
        fread(&DATA_base, sizeof(First), 1, fout);
        while (!feof(fout))
        {
            if (DATA_base.pos.pos_name == users_pos)
            {
                Data_massive[a] = DATA_base;
                a++;
            }
            fread(&DATA_base, sizeof(First), 1, fout);
        }
        fclose(fout);
    }

    if (a == 0)
        cout << "No job title founded";

    for (int i = 0; i < a; i++)
    {
        cout << endl << "Firm -> " << Data_massive[i].firm << endl << "Job title requriments -> " << Data_massive[i].pos.vymogi << endl << "----------------------------------------------";
    }
}

void new_mas_str()
{
    fout = fopen("binary_meme.txt", "rb");
    int a = 0;
    First DATA_base;
    First Data_massive[100];
    int help_massive[100];
    New_First New_Data[100];
    float sum = 0;
    int count_1 = 0;
    int count_2 = 0;
    if (!(fout = fopen("binary_meme.txt", "rb")))
        cerr << "File do not exist!";
    else
    {
        fread(&DATA_base, sizeof(First), 1, fout);
        while (!feof(fout))
        {
            Data_massive[a] = DATA_base;
            a++;
            fread(&DATA_base, sizeof(First), 1, fout);
        }
        fclose(fout);
    }
    for (int i = 0; i < a; i++)
    {
        if (help_massive[i] == 0)
            continue;
        New_Data[count_1].new_vac = Data_massive[i].pos.pos_name;
        for (int j = i; j < a; j++)
        {
            if (Data_massive[i].pos.pos_name == Data_massive[j].pos.pos_name)
            {
                sum += Data_massive[j].robot.zarplata;
                count_2++;
                help_massive[j] = 0;
            }
        }
        New_Data[count_1].new_zp = sum / count_2;
        count_1++;
        sum = 0;
        count_2 = 0;
    }
    for (int i = 0; i < count_1; i++)
    {
        cout << endl << "Job title -> " << New_Data[i].new_vac << endl << "Average salary -> " << New_Data[i].new_zp << endl << "----------------------------------------------";
    }

}

int main()
{
    while (true)
    {
        menu();
        int key;
        cin >> key;
        switch (key)
        {
        case 1:
        {
            input();
            system("cls");
            break;
        }
        case 2:
        {
            output();
            cout << endl << "Press enter";
            getch();
            system("cls");
            break;
        }
        case 3:
        {
            delete_all_data();
            system("cls");
            break;
        }
        case 4:
        {
            remove_data();
            cout << endl << "Press enter";
            getch();
            system("cls");
            break;
        }
        case 5:
        {
            replace_data();
            cout << endl << "Press enter";
            getch();
            system("cls");
            break;
        }
        case 6:
        {
            bigger_vacantions();
            cout << endl << "Press enter";
            getch();
            system("cls");
            break;
        }
        case 7:
        {
            vymogy_for_vac();
            cout << endl << "Press enter";
            getch();
            system("cls");
            break;
        }
        case 8:
        {
            new_mas_str();
            cout << endl << "Press enter";
            getch();
            system("cls");
            break;
        }
        case 0:
        {
            exit(0);
        }
        }
    }

    return 0;
}
