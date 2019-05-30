#include <cmath> //мат функции
#include <iostream>
#include <vector>

using namespace std;

float mod_exp(int para);
float  FloatRand(float _max, float _min);

//setlocale( LC_ALL, "Russian");

int main()
{
	setlocale(LC_ALL, "Russian");
	float T0 = 0;
	float T[4] = { 0,0,0,0 }; //все занулим, наши каналы 
	int lambda = 3;
	int mu = 1;
	vector <float > wait; //храним время, когда пришла заявка и попала в очередь 
	int amount = 0; //суммарное количество людей в очереди 

	int n = 0;//количество всех зявок в очереди
	float time = 0; //суммарное время ожидания

	float av_time = 0;

	for (int i = 0; i < 10; i++)//1000 реализаций 
	{
		//T0 = 0;
		while (T0 < 10) //работа на интервале от 0 до 1000
		{
			//cout << "T0 " << T0 << " time: " << time <<" n: "<<n<< endl;
			T0 = T0 + mod_exp(lambda); //моделируем приход новой заявки 
			if (T0 < 10) //если пришла до 1000 сек
			{
				//cout << "kek "<< i<< "   TO   "<<T0 << endl;
				int j = 0;
				int num = 0;
				bool flag = false;
				for (j; j < 4; j++) //смотрим, есть ли свободный канал 
				{
					if (T0 > T[j]) //есть ли свободный канал
					{
						num = j;//запоминаем номер
						flag = true;
						break;//заканчиваем искать свободный канал 
					}
					//else flag = false;
				}

				if (flag && wait.empty()) //если есть свободный канал и нет никого в очереди 
				{
					//cout << "Num: " << num << " T num " << T[num]<< "  "<<T0 << endl;;
					time = time + 0;
					T[num] = T0 + mod_exp(mu);//идет на обслуживание 
					n++;
				}

				else if (flag  && (!wait.empty())) //если есть свободный канал, есть заявка в очереди  
				
				{
					cout << "CHECK: " << T0 << endl;
					T[num] = T0 + mod_exp(mu);//идет на обслуживание заявка из очереди
					time = time + (T0 - wait[0]);
					wait.erase(wait.begin());
					wait.push_back(T0); //записываем в вектор время прихода заявки, отправляем в очередь в конец
					n++;
				}
				
				else if (!flag) //если нет свободных каналов
				{
					wait.push_back(T0);//запихиваем в очередь
					n++;
				}
			}
			else
			{
				T0 = 0;
				n = n - wait.size();
				wait.erase(wait.begin(), wait.end());
				break;
			}
			//cout << n << endl;
			/*for (int g = 0; g < wait.size(); g++)
				time = time + 1000 - wait[g];*/
		}
		//if (!wait.empty()) {
		//	for (int g = 0; g < wait.size(); g++) {
		//		//cout << "wait: " << wait[g] <<"   "<<wait.size() << endl;
		//		//cout << "Time: " << time << " T0: " << T0 << " wait[g]: " << wait[g] << endl;
		//		time = time + (1000 - wait[g]);
		//		//cout << time << endl;
		//	}
		//}
		//T0 = 0;
		//cout << "n: " << n << " size: " << wait.size() << endl;
		//n = n - wait.size();
		//cout << "n: " << n << " size: " << wait.size() << endl;
		wait.erase(wait.begin(), wait.end()); //очищаем вектор 
	}

	cout << "Time: " << time << " Num: " << n << endl;
	av_time = time / n; //общее время ожидания делим на общее количество 
	cout << endl<<"Среднее время ожидания: " << av_time << endl;
	

}


float mod_exp(int param)
{
	float k=0;
	float a = 0;
	a = FloatRand(1, 0); //рандомное число от 0 до 1

	k = (-1)*(1. / param)*log(a);
	return k;
}


float  FloatRand(float _max, float _min)
{
	return _min + float(rand()) / RAND_MAX * (_max - _min);
}

