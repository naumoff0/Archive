#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>
#include <direct.h>
#include <sstream>
#include <vector>
#include <iterator>
#include <filesystem>
#include "dirent.h"
#include <windows.h>
#include <conio.h>

//create a directory file and store the users directory in it for later use
std::string getUserDirectory() {
    std::string directory = "";
    if (!std::ifstream("userDirectory.txt")) {
        std::cout << "If you have gotten this message it means you have not specified a directory.\n";
        std::cout << "In order for this program to work you need to specify the directory in which you located the executable.\n";
        std::cout << "Please enter the executable using double back slashes. \n";
        std::cout << "An Example: C:\\\\Users\\User1\\\\Desktop\\\\R.C.S\\\\     <-- remember those last two \\\\ \n";
        std::cout << "Warning, if you screw this up, please delete the existing file created called userDirectory.txt and restart the program. \n";
        std::cout << "Directory: ";
        std::cin >> directory;

        std::ofstream dirFile;
        dirFile.open("userDirectory.txt", std::ios::app);

        dirFile << directory;
    }

    std::ifstream dirFile("userDirectory.txt");
    directory = "";
    if (!dirFile.is_open()) std::cerr << "Unable to open file.\n";
    dirFile >> directory;

    return directory;
}
//ask user for the report card and subject to make a final directory for file i/o
std::string generateDirectory() {
    // More on this later
    std::cin.ignore();
    std::ostringstream combinedDirectory;
    std::string chosenReportCard = "";
    std::string chosenSubject = "";

    std::cout << "\nEnter report card name: ";
    getline(std::cin, chosenReportCard);
    combinedDirectory << getUserDirectory() << chosenReportCard;
    std::cout << "\nEnter the subject: ";
    getline(std::cin, chosenSubject);

    // create a subject directory based on input from user to enter grades into
    combinedDirectory << "\\" << chosenSubject << ".txt";
    std::string subjectDir = combinedDirectory.str();

    return subjectDir;
}
//template 1 called the 'regular'
static const std::string template1[] = { "Physical Education",
"Technology/Engineer", "Language Arts",
"Math", "Social Studies", "Science"

};
//template 2 called the 'mathematician'
static const std::string template2[] = { "Math", "Science", "Technology",
"Programming" };
//template 3 called the 'philosopher'
static const std::string template3[] = { "Art", "Social Studies",
"Language Arts", "Philosophy",

"Medieval World Studies" };

//allows users to add subjects themsevles and name them or use one of the tempates above
void addSubjects(int choice, std::string reportCardName) {
    if (choice == 1) {
        std::cout << "Input the number of subjects you would like to add: ";
        int numSubjects = 0;
        std::cin >> numSubjects;
        std::cout << "\n";

        for (int i = 0; i < numSubjects; i++) {
            std::cout << "Input the name of subject " << i+1 << ": ";
            std::string subject = "";
            std::cin >> subject;
            std::ostringstream path;
            path << getUserDirectory() << reportCardName << "\\" << subject << ".txt";
            std::string saveLocation = path.str();
            std::ofstream outfile(saveLocation.c_str());
            std::cout << subject << " is now a subject!" << std::endl;
        }
    } 
    else if (choice == 2) {
        std::cout << "Choose a template:\n";
        std::cout << "1)The Regular (all the basics, P.E, Math, Science etc.)\n";
        std::cout << "2)The Mathematician (Math, Science, Tech etc.)\n";
        std::cout << "3)The Philosopher (Social Studies, Language Arts, Art etc.)\n";
        std::cout << "More Coming Soon!\n";
        std::cout << "Template Selected: ";
        std::cin >> choice;

        switch (choice) {
        case 1:

            for (int i = 0; i <= 5; i++) {
                std::ostringstream path;
                path << getUserDirectory() << reportCardName << "\\" << template1[i] << ".txt";
                std::string saveLocation = path.str();
                std::ofstream outfile(saveLocation.c_str());
                std::cout << "\n" << template1[i] << " Is now a subject!";
            }
            break;

        case 2:

            for (int i = 0; i <= 3; i++) {
                std::ostringstream path;
                path << getUserDirectory() << reportCardName << "\\" << template2[i] << ".txt";
                std::string saveLocation = path.str();
                std::ofstream outfile(saveLocation.c_str());
                std::cout << "\n" << template2[i] << " Is now a subject!";
            }

            break;

        case 3:

            for (int i = 0; i <= 3; i++) {
                std::ostringstream path;
                path << getUserDirectory() << reportCardName << "\\" << template3[i] << ".txt";
                std::string saveLocation = path.str();
                std::ofstream outfile(saveLocation.c_str());
                std::cout << "\n" << template3[i] << " Is now a subject!";
            }

            break;
        }
    }

}

//allows user to add subjects to an already existing report card
void addNewSubjects() {
        std::cin.ignore();
        int choice = 0;
        std::string reportCardName;
        std::cout << "\nEnter report card name: ";
        std::getline(std::cin, reportCardName);

        int newSubjectAmount = 0;
        std::cout << "Input amount of new subjects to be created: ";
        std::cin >> newSubjectAmount;

        for (int i = 0; i < newSubjectAmount; i++) {
            std::cout << "Input the name of subject " << i + 1 << ": ";
            std::string newSubject = "";
            std::cin >> newSubject;
            std::ostringstream path;
            path << getUserDirectory() << reportCardName << "\\" << newSubject << ".txt";
            std::string saveLocation = path.str();
            std::ofstream outfile(saveLocation.c_str());
            std::cout << newSubject << " is now a subject!" << std::endl;
        }
}

//for generating a folder to store subjects 
void generateReportCard() {
    std::cin.ignore();
    int choice = 0;
    std::string reportCardName;
    std::cout << "\nEnter report card name: ";
    std::getline(std::cin, reportCardName);
    _mkdir(reportCardName.c_str());  // make folder for report card
    std::cout << "\nYou successfully made a report card!\n";
    std::cout << "Would you like to:\n";
    std::cout << "1)Add subjects to it\n";
    std::cout << "2)Use a template?\n";
    std::cout << "(note you can only do this once)\n";
    std::cout << "1 or 2: ";
    std::cin >> choice;
    std::cout << "\n";
    addSubjects(choice, reportCardName);
}

//enables user to edit subjects and add assignments + grades into subject txt file
void enterGrades(int scoresToEnter) {
    std::ofstream subject;
    subject.open(generateDirectory().c_str(), std::ios::app);
    std::cout << "\nWarning! Please only enter grades based on percentage out of 100 (please don't use %'s)\n";
    std::cout << "Press enter to continue.\n";
    std::cin.ignore();
    for (int i = 0; i < scoresToEnter; ++i) {
        std::string assignmentName = "";
        std::cout << "\nEnter assignment name: ";
        getline(std::cin, assignmentName);

        std::string grade = "";
        std::cout << "\nEnter grade: ";
        getline(std::cin, grade);

        std::string subjectEntry = assignmentName + " " + grade;

        subject << subjectEntry << std::endl;
    }
}

// calculate subject card average and display it
void printSubject() {
    std::ifstream subject(generateDirectory().c_str());

    if (!subject.is_open()) std::cerr << "Unable to open file.\n";

    std::string line;
    std::vector<std::string> assignmentList = {};
    std::vector<double> gradeList = {};
    std::string assignmentName = "";
    double score = 0;
    double avg = 0;
    int counter = 0;

    while (subject >> assignmentName >> score) {
        assignmentList.push_back(assignmentName);
        gradeList.push_back(score);
        avg += score;
        assignmentName = "";
        counter++;
    }

    avg = avg / counter;
    std::cout << "\n----------------------------------------------------\n";
    for (int i = 0; i < assignmentList.size(); ++i) {
        std::cout << "Assignment: " << assignmentList[i] << " || Score " << gradeList[i] << std::endl;
    }
    std::cout << "\n------------------\n";
    std::cout << "Average grade is: " << avg;
    std::cout << "\n----------------------------------------------------\n";
}

//gives a report of the entire report card
void giveReport() {
    std::cout << "\nNote that subjects must have atleast 1 assignment minimum to give final report.\n\n";
    std::string reportCardName = "";
    std::cin.ignore();
    std::cout << "Enter name of report card: ";
    getline(std::cin, reportCardName);
    std::ostringstream path;
    path << getUserDirectory() << reportCardName;
    std::string location = path.str();

    std::vector<std::string> fileNames = {};
    DIR *dir;
    struct dirent *ent;
    if ((dir = opendir(location.c_str())) != NULL) {
        int counter = 0;
        while ((ent = readdir(dir)) != NULL) {
            if (counter > 1) fileNames.push_back(ent->d_name);
            counter++;
        }
    }

    std::string tempLocation;
    double score;
    double avg;
    int avgIterator;
    double totalAvg = 0;
    int totalAvgIterator = 0;
    std::string ignoreName = "";
    std::cout << "\n------------------\n";

    for (int i = 0; i < fileNames.size(); i++) {
        tempLocation = "";
        std::ostringstream tempPath;

        tempPath << getUserDirectory() << reportCardName << "\\" << fileNames[i];
        tempLocation = tempPath.str();

        score = 0;
        avg = 0;
        avgIterator = 0;

        std::ifstream subject(tempLocation.c_str());
        if (!subject.is_open()) {
            std::cerr << "Unable to open file " << tempLocation << " to read from\n";
            continue;
        }

        while (subject >> ignoreName >> score) {
            avg += score;
            totalAvg += score;
            avgIterator++;
            totalAvgIterator++;
            ignoreName = "";
        }

        avg = avg / avgIterator;
        std::cout << "\nSubject: " << fileNames[i] << " || Average score: " << avg;

        subject.close();
        subject.clear();
    }
    totalAvg = totalAvg / totalAvgIterator;
    std::cout << "\n------------------\n";
    std::cout << "Total average grade is: " << totalAvg;
    std::cout << "\n----------------------------------------------------\n";

    closedir(dir);
}

//allows user to delete a single subject and all it's data
void deleteSubject() {
    std::string reportCardName = "";
    std::string subjectName = "";

    std::cout << "\nEnter the name report card where the subject is located: ";
    std::cin >> reportCardName;
    std::cout << "\nEnter the name of the subject: ";
    std::cin >> subjectName;

    std::ostringstream path;
    path << getUserDirectory() << reportCardName << "\\" << subjectName << ".txt";
    std::string subjectLocation = path.str();

    if (remove(subjectLocation.c_str()) != 0) std::cout << "\nError, could not delete file.\n";
    else std::cout << "\n" << subjectName << " Succsessfully deleted!\n";

}
//credits to stack overflow for providing me with this function that doesn't force me to use boost
int DeleteDirectory(const std::string &refcstrRootDirectory,
    bool              bDeleteSubdirectories = true)
{
    bool            bSubdirectory = false;       // Flag, indicating whether
                                                 // subdirectories have been found
    HANDLE          hFile;                       // Handle to directory
    std::string     strFilePath;                 // Filepath
    std::string     strPattern;                  // Pattern
    WIN32_FIND_DATA FileInformation;             // File information


    strPattern = refcstrRootDirectory + "\\*.*";
    hFile = ::FindFirstFile(strPattern.c_str(), &FileInformation);
    if (hFile != INVALID_HANDLE_VALUE)
    {
        do
        {
            if (FileInformation.cFileName[0] != '.')
            {
                strFilePath.erase();
                strFilePath = refcstrRootDirectory + "\\" + FileInformation.cFileName;

                if (FileInformation.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)
                {
                    if (bDeleteSubdirectories)
                    {
                        // Delete subdirectory
                        int iRC = DeleteDirectory(strFilePath, bDeleteSubdirectories);
                        if (iRC)
                            return iRC;
                    }
                    else
                        bSubdirectory = true;
                }
                else
                {
                    // Set file attributes
                    if (::SetFileAttributes(strFilePath.c_str(),
                        FILE_ATTRIBUTE_NORMAL) == FALSE)
                        return ::GetLastError();

                    // Delete file
                    if (::DeleteFile(strFilePath.c_str()) == FALSE)
                        return ::GetLastError();
                }
            }
        } while (::FindNextFile(hFile, &FileInformation) == TRUE);

        // Close handle
        ::FindClose(hFile);

        DWORD dwError = ::GetLastError();
        if (dwError != ERROR_NO_MORE_FILES)
            return dwError;
        else
        {
            if (!bSubdirectory)
            {
                // Set directory attributes
                if (::SetFileAttributes(refcstrRootDirectory.c_str(),
                    FILE_ATTRIBUTE_NORMAL) == FALSE)
                    return ::GetLastError();

                // Delete directory
                if (::RemoveDirectory(refcstrRootDirectory.c_str()) == FALSE)
                    return ::GetLastError();
            }
        }
    }

    return 0;
}
//allows user to delete a report card with all it's subjects using the function above
void deleteReportCard() {
    std::string reportCardName = "";
    std::cout << "Enter report card name: ";
    std::cin >> reportCardName;

    std::ostringstream path; 
    path << getUserDirectory() << reportCardName;
    std::string location = path.str();

    int iRC = 0;

    iRC = DeleteDirectory(location);

    if (iRC){
        std::cout << "Error " << iRC << std::endl;
    }

}

//main menu giving access to all the functions above
void mainMenu() {
    std::cout << "\nPlease select an option below\n";
    std::cout << "1) Create a report card or create more subjects\n";
    std::cout << "2) Enter grades into a subject\n";
    std::cout << "3) Get a report for a report card and/or subject\n";
    std::cout << "4) Delete a report card or subject\n";
    std::cout << "Option Selected: ";

    int choice = 0;
    std::cin >> choice;

    // check for user choice then execute a function based on that choice
    int numAssignments = 0;
    std::string giveNewReport;
    std::string printNewSubject;
    std::string runAgain;
    std::string subjectDelete = "";
    std::string reportCardDelete = "";
    switch (choice) {
    case 1:
        choice = 0;
        std::cout << "\nSelect an option below\n";
        std::cout << "1) Create a report card then add subjects too it\n";
        std::cout << "2) Add subjects to an existing report card\n";
        std::cout << "Choice: ";
        std::cin >> choice;
        if (choice == 1) {
            for (;;) {
                generateReportCard();
                std::cout << "\n\nWould you like to create another report card? (y/n): ";
                runAgain = "";
                std::cin >> runAgain;
                if (runAgain != "y") break;
            }
        }
        else if (choice == 2) {
            for (;;) {
                addNewSubjects();
                std::cout << "\n\nWould you like to add more subjects to another report card? (y/n): ";
                runAgain = "";
                std::cin >> runAgain;
                if (runAgain != "y") break;
            }
        }
        break;
    case 2:
        std::cout << "How many scored assignments would you like to enter? ";
        std::cin >> numAssignments;
        enterGrades(numAssignments);

        break;

    case 3:
        choice = 0;
        std::cout << "\nSelect an option below\n";
        std::cout << "1) Disply the average for every subject in a report card and a final average\n";
        std::cout << "2) Display the average for only 1 subject\n";
        std::cout << "Choice: ";
        std::cin >> choice;

        if (choice == 1) {
            for (;;) {
                giveReport();
                giveNewReport = "";
                std::cout << "Would you like to get a report from another report "
                    "card? (y/n):";
                std::cin >> giveNewReport;
                if (giveNewReport != "y") break;
            }

        }
        else if (choice == 2) {
            for (;;) {
                printSubject();
                printNewSubject = "";
                std::cout << "Would you like to print out another subject? (y/n):";
                std::cin >> printNewSubject;
                if (printNewSubject != "y") break;
            }
            if (choice != 1 && choice != 2) std::cout << "Error, that is not a valid choice. \n";
        }
        break;
    case 4:
        choice = 0;
        std::cout << "\nSelect an option below\n";
        std::cout << "1) Delete a subject\n";
        std::cout << "2) Delete a report card\n";
        std::cout << "Choice: ";
        std::cin >> choice;

        if (choice == 1) {
            for (;;) {
                deleteSubject();
                subjectDelete = "";
                std::cout << "Would you like to delete another subject? (y/n): ";
                std::cin >> subjectDelete;

                if (subjectDelete != "y") break;

            }

        }
        else if (choice == 2) {
            for (;;) {
                deleteReportCard();
                reportCardDelete = "";
                std::cout << "Would you like to delete another report card? (y/n): ";
                std::cin >> reportCardDelete;

                if (reportCardDelete != "y") break;
            }

            if (choice != 1 && choice != 2) std::cout << "Error, that is not a valid choice. \n";

            break;
        }
    }
}

int main() {
    getUserDirectory();
    for (;;) {
        mainMenu();
        std::string backToMainMenu = "";
        std::cout << "Return back to main menu? n will shutdown the program (y/n): ";
        std::cin >> backToMainMenu;
        if (backToMainMenu != "y") break;
    }
    return 0;
}
