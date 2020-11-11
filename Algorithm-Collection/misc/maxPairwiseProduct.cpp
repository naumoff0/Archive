#include <iostream>
#include <vector>
#include <random>
#include <windows.h>

double PCFreq = 0.0;
__int64 CounterStart = 0;


long long MaxPairwiseProduct(std::vector<int>& numbers)
{
    int n = numbers.size();
    int firstIndex = 0, secondIndex = n - 1;

    for (int i = 1; i < n; ++i)
    {
        // scan array incrementing
        if (numbers[i] > firstIndex && i != secondIndex)
            firstIndex = i;


        // scan array decrementing
        if (numbers[n - (i + 1)] > secondIndex && n - (i + 1) != firstIndex)
            secondIndex = n - (i + 1);
    }

    return (long long)numbers[firstIndex] * (long long)numbers[secondIndex];
}


long long MaxPairwiseProductNaive(std::vector<int>& numbers)
{
    int n = numbers.size();
    int firstIndex = 0;

    // first scan
    for (int i = 1; i < n; ++i)
    {
        if (numbers[i] > numbers[firstIndex])
            firstIndex = i;
    }

    int secondIndex = 0;
    if (firstIndex == 0)
        secondIndex = 1;

    // second scan
    for (int i = 1; i < n; ++i)
    {
        if (i != firstIndex && numbers[i] > numbers[secondIndex])
            secondIndex = i;
    }

    return (long long)numbers[firstIndex] * (long long)numbers[secondIndex];
}


void StartCounter()
{
    LARGE_INTEGER li;

    if (!QueryPerformanceFrequency(&li))
        std::cout << "QueryPerformanceFrequency failed!\n";

    PCFreq = double(li.QuadPart);

    QueryPerformanceCounter(&li);
    CounterStart = li.QuadPart;
}


double GetCounter()
{
    LARGE_INTEGER li;

    QueryPerformanceCounter(&li);
    return double(li.QuadPart - CounterStart) / PCFreq;
}


std::vector<int> generateRandomNumbers(int maxSetLength, int bound)
{
    std::random_device rd;
    std::mt19937 rng(rd());

    std::uniform_int_distribution<int> setLength(2, maxSetLength);
    std::uniform_int_distribution<int> number(1, bound);
    std::vector<int> numbers(setLength(rng));

    for (int i = 0; i < static_cast<int>(numbers.size()); ++i)
        numbers[i] = number(rng);

    return numbers;
}


void stressTest()
{
    std::cout << "Generating the dataset..." << std::endl;
    int maxSetLength = 3;
    int bound = 100000;
    int size = 1000000;

    std::vector<std::vector<int> > dataSet;

    for (int i = 0; i < size; ++i)
        dataSet.push_back(generateRandomNumbers(maxSetLength, bound));

    std::cout << "Starting tests..." << std::endl;
    // stress test naive
    StartCounter();
    for (int i = 0; i < static_cast<int>(dataSet.size()); ++i)
        MaxPairwiseProductNaive(dataSet[i]);

    std::cout << "NAIVE: " << GetCounter() << "\n";

    // stress test current
    StartCounter();
    for (int i = 0; i < static_cast<int>(dataSet.size()); ++i)
        MaxPairwiseProduct(dataSet[i]);

    std::cout << "CURRENT: " << GetCounter() << "\n";
}


std::vector<int> humanInput()
{
    int n;

    std::cin >> n;
    std::vector<int> numbers(n);
    for (int i = 0; i < n; ++i)
    {
        std::cin >> numbers[i];
    }

    return numbers;
}


int main()
{
    /**
       std::vector<int> numbers = humanInput();
       long long product = MaxPairwiseProduct(numbers);
       std::cout << product << "\n";
     **/

    stressTest();

    return 0;
}
