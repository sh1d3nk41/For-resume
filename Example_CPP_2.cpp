#include <iostream>
#include <queue>
#include <cstdlib>
#include <ctime>


using namespace std;

struct Data
{
	float hit_points = 0.0;
	float damage = 0.0;
	int skill_level = 0;
	Data()
	{
		float hit_points = rand() % 100;
		float damage = rand() % 100;
		int skill_level = rand() % 100;
	}
	bool operator>(const Data& One_Data) const
	{
		if (skill_level != One_Data.skill_level)
		{
			return skill_level < One_Data.skill_level;
		}
		if (hit_points != One_Data.hit_points)
		{
			return hit_points < One_Data.hit_points;
		}
		if (damage != One_Data.damage)
		{
			return damage < One_Data.damage;
		}
	}

	bool operator<(const Data& One_Data) const
	{
		if (skill_level != One_Data.skill_level)
		{
			return skill_level > One_Data.skill_level;
		}
		if (hit_points != One_Data.hit_points)
		{
			return hit_points > One_Data.hit_points;
		}
		if (damage != One_Data.damage)
		{
			return damage > One_Data.damage;
		}
	}

	bool operator==(const Data& One_Data) const
	{
		if (hit_points == One_Data.hit_points)
		{
			return hit_points == One_Data.hit_points;
		}
		if (damage == One_Data.damage)
		{
			return damage == One_Data.damage;
		}
		if (skill_level == One_Data.skill_level)
		{
			return skill_level == One_Data.skill_level;
		}
	}

};

struct PriorityQueue
{
	vector<Data> AllData;
	int last = 0;
	int getParent(int index)
	{
		return (index - 1) / 2;
	}
	int getLeftChild(int index)
	{
		return 2 * index + 1;
	}
	int getRightChild(int index)
	{
		return 2 * index + 2;
	}
	void siftUp(int index)
	{
		int Elem_Up = index;
		while (AllData[getParent(Elem_Up)] > AllData[Elem_Up] && Elem_Up != 0)
		{
			swap(AllData[getParent(Elem_Up)], AllData[Elem_Up]);
			Elem_Up = getParent(Elem_Up);
		}
	}
	void siftDown(int index)
	{
		int Elem_Down = index;
		while (getLeftChild(Elem_Down) < last && getRightChild(Elem_Down) < last)
		{
			if (AllData[getLeftChild(Elem_Down)] > AllData[getRightChild(Elem_Down)])
			{
				swap(AllData[getLeftChild(Elem_Down)], AllData[Elem_Down]);
				Elem_Down = getLeftChild(Elem_Down);
			}
			else
			{
				swap(AllData[getRightChild(Elem_Down)], AllData[Elem_Down]);
				Elem_Down = getRightChild(Elem_Down);
			}
		}

	}
	void push(Data object_in)
	{
		AllData.push_back(object_in);
		siftUp(last);
		last++;
	}
	Data top()
	{
		return AllData[0];
	}
	void pop()
	{
		swap(AllData[0], AllData[last - 1]);
		AllData.pop_back();
		siftDown(0);
		last--;
	}
	int size()
	{
		return last - 1;
	}
	bool empty()
	{
		if (size() == 0)
			return true;
		else
		{
			return false;
		}

	}

};

template <typename T>
float testPriorityQueueSpeed(T&& priorityQueue)
{
	const int iters = 100000;
	clock_t timeStart = clock();
	for (int i = 0; i < iters; i++)
	{
		cout << " 1 ";
		int insertDataAmount = rand() % 6 + 5;
		for (int j = 0; j < insertDataAmount; j++)
		{
			priorityQueue.push(Data());
		}
		priorityQueue.top();
		priorityQueue.pop();
	}
	clock_t timeEnd = clock();
	float time = (float(timeEnd - timeStart)) / CLOCKS_PER_SEC;
	return time;
}
bool testPriorityQueue()
{
	srand(time(NULL));
	const int iters = 20000;
	PriorityQueue myPriorQueue;

	priority_queue<Data> stlPriorQueue;
	bool isDataEqual = true;
	for (int i = 0; i < iters; i++)
	{
		int insertDataAmount = rand() % 6 + 5;
		for (int j = 0; j < insertDataAmount; j++)
		{
			Data randData = Data();
			myPriorQueue.push(randData);
			stlPriorQueue.push(randData);
		}
		if (!(myPriorQueue.top() == stlPriorQueue.top()))
		{
			isDataEqual = false;
			cerr << "Comparing failed on iteration " << i << endl << endl;
			break;
		}
		int removeDataAmount = rand() % insertDataAmount;
		for (int j = 0; j < removeDataAmount; j++)
		{
			myPriorQueue.pop();
			stlPriorQueue.pop();
		}
	}
	int myQueueSize = myPriorQueue.size();
	int stlQueueSize = stlPriorQueue.size();
	float stlTime =
		testPriorityQueueSpeed<priority_queue<Data>>(priority_queue<Data>());
	float myTime = testPriorityQueueSpeed<PriorityQueue>(PriorityQueue());
	cout << "My PriorityQueue:" << endl;
	cout << "Time: " << myTime << ", size: " << myQueueSize << endl;
	cout << "STL priority_queue:" << endl;
	cout << "Time: " << stlTime << ", size: " << stlQueueSize << endl << endl;
	if (isDataEqual && myQueueSize == stlQueueSize)
	{
		cout << "The lab is completed" << endl << endl;
		return true;
	}
	cerr << ":(" << endl << endl;
	return false;
}

int main()
{
	testPriorityQueue();
	return 0;
}
