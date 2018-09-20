#include <iostream>
#include <vector>
#include <string.h>
#include <windows.h>

using namespace std;

class Piece {
    private:
        int x, y;
        string color;
    public:
        Piece (int x_pos, int y_pos, string c){
            x = x_pos;
            y = y_pos;
            color = c;
        }
        int getx() {return x;}
        int gety() {return y;}
        string getColor() {return color;}
        void setColor(string c) {color = c;}
        void set (int x_pos, int y_pos, string c) {
            x = x_pos;
            y = y_pos;
            color = c;
        }
        void flip() {
            if (color == "black") {color = "white";}
            else {color = "black";}
        }
};

class Board {
    private:
        vector<Piece> list;         ///Vector of existing pieces
        Piece getPiece(int x, int y) {      ///Returns piece at location
            for (int i=0; i<list.size(); i++) {
                if (list.at(i).getx() == x && list.at(i).gety() == y) {return list.at(i);}
            }
        }
        int getIndex(int x, int y) {        ///Returns vector index of piece at location
            for(int i=0; i<list.size(); i++) {
                if (list.at(i).getx() == x && list.at(i).gety() == y) {return i;}
            }
        }
        int getBlackNum () {            ///Returns # of black pieces
            int num = 0;
            for (int i=0; i<list.size(); i++) {
                if (list.at(i).getColor().compare("black") == 0) {num++;}
            }
            return num;
        }
        int getWhiteNum () {            ///Returns # of white pieces
            int num = 0;
            for (int i=0; i<list.size(); i++) {
                if (list.at(i).getColor().compare("white") == 0) {num++;}
            }
            return num;
        }
        void display() {               ///Displays board state
            cout << "   Board" << endl << "   +---+---+---+---+---+---+---+---+" << endl;
            for (int y=8; y>=1; y--) {
                cout << " " << y << " | ";
                for (int x=1; x<=8; x++) {
                    if (pAtLoc(x, y)) {
                        if (getPiece(x, y).getColor()=="black") {cout << "b";}
                        else if (getPiece(x, y).getColor()=="white") {cout << "w";}
                    }
                    else {
                        cout << " ";
                    }
                    cout << " | ";
                }
                cout << endl << "   +---+---+---+---+---+---+---+---+" << endl;
            }
            cout << "     1   2   3   4   5   6   7   8  " << endl << endl;
        }
        bool pAtLoc(int x, int y) {      ///Checks for existence of piece at location
            for (int i=0; i<list.size(); i++) {
                if (list.at(i).getx()==x && list.at(i).gety()==y) {
                    return true;
                }
            }
            return false;
        }
        bool inRange(int x, int y) {     ///Checks if location is on the board
            return !(x<1 || x>8 || y<1 || y>8);
        }
        bool legalDown(int x, int y, string color) {
            int currenty;

            if (pAtLoc(x, y-1)) {
                if (getPiece(x, y-1).getColor().compare(color) != 0) {
                    currenty = y-1;
                    while (pAtLoc(x, currenty-1)) {
                        if (getPiece(x, currenty-1).getColor().compare(color) == 0) {return true;}
                        else {
                            currenty--;
                        }
                    }
                }
            }
            return false;
        }
        bool legalUp(int x, int y, string color) {
            int currenty;

            if (pAtLoc(x, y+1)) {
                if (getPiece(x, y+1).getColor().compare(color) != 0) {
                    currenty = y+1;
                    while (pAtLoc(x, currenty+1)) {
                        if (getPiece(x, currenty+1).getColor().compare(color) == 0) {return true;}
                        else {
                            currenty++;
                        }
                    }
                }
            }
            return false;
        }
        bool legalLeft(int x, int y, string color) {
            int currentx;

            if (pAtLoc(x-1, y)) {
                if (getPiece(x-1, y).getColor().compare(color) != 0) {
                    currentx = x-1;
                    while (pAtLoc(currentx-1, y)) {
                        if (getPiece(currentx-1, y).getColor().compare(color) == 0) {return true;}
                        else {
                            currentx--;
                        }
                    }
                }
            }
            return false;
        }
        bool legalRight(int x, int y, string color) {
            int currentx;

            if (pAtLoc(x+1, y)) {
                if (getPiece(x+1, y).getColor().compare(color) != 0) {
                    currentx = x+1;
                    while (pAtLoc(currentx+1, y)) {
                        if (getPiece(currentx+1, y).getColor().compare(color) == 0) {return true;}
                        else {
                            currentx++;
                        }
                    }
                }
            }
            return false;
        }
        bool legalUpLeft(int x, int y, string color) {
            int currentx, currenty;

            if (pAtLoc(x-1, y+1)) {
                if (getPiece(x-1, y+1).getColor().compare(color) != 0) {
                    currentx = x-1;
                    currenty = y+1;
                    while (pAtLoc(currentx-1, currenty+1)) {
                        if (getPiece(currentx-1, currenty+1).getColor().compare(color) == 0) {return true;}
                        else {
                            currentx--;
                            currenty++;
                        }
                    }
                }
            }
            return false;
        }
        bool legalUpRight(int x, int y, string color) {
            int currentx, currenty;

            if (pAtLoc(x+1, y+1)) {
                if (getPiece(x+1, y+1).getColor().compare(color) != 0) {
                    currentx = x+1;
                    currenty = y+1;
                    while (pAtLoc(currentx+1, currenty+1)) {
                        if (getPiece(currentx+1, currenty+1).getColor().compare(color) == 0) {return true;}
                        else {
                            currentx++;
                            currenty++;
                        }
                    }
                }
            }
            return false;
        }
        bool legalDownRight(int x, int y, string color) {
            int currentx, currenty;

            if (pAtLoc(x+1, y-1)) {
                if (getPiece(x+1, y-1).getColor().compare(color) != 0) {
                    currentx = x+1;
                    currenty = y-1;
                    while (pAtLoc(currentx+1, currenty-1)) {
                        if (getPiece(currentx+1, currenty-1).getColor().compare(color) == 0) {return true;}
                        else {
                            currentx++;
                            currenty--;
                        }
                    }
                }
            }
            return false;
        }
        bool legalDownLeft(int x, int y, string color) {
            int currentx, currenty;

            if (pAtLoc(x-1, y-1)) {
                if (getPiece(x-1, y-1).getColor().compare(color) != 0) {
                    currentx = x-1;
                    currenty = y-1;
                    while (pAtLoc(currentx-1, currenty-1)) {
                        if (getPiece(currentx-1, currenty-1).getColor().compare(color) == 0) {return true;}
                        else {
                            currentx--;
                            currenty--;
                        }
                    }
                }
            }
            return false;
        }
        bool legalMove(int x, int y, string color) {        ///Checks if legal move exists at location for specific color
            if (pAtLoc(x, y)|| !inRange(x, y)) {return false;}
            return legalDown(x, y, color) || legalUp(x, y, color) || legalLeft(x, y, color) || legalRight(x, y, color) || legalUpLeft(x, y, color) || legalUpRight(x, y, color) || legalDownRight(x, y, color) || legalDownLeft(x, y, color);
        }
        void placePiece(int x, int y, string color) {       ///Places piece and flips as needed
            int currentx, currenty;

            if (legalDown(x, y, color)) {
                currenty = y-1;
                while(getPiece(x, currenty).getColor().compare(color) != 0) {
                    list.at(getIndex(x, currenty)).flip();
                    currenty--;
                }
            }
            if(legalUp(x, y, color)) {
                currenty = y+1;
                while(getPiece(x, currenty).getColor().compare(color) != 0) {
                    list.at(getIndex(x, currenty)).flip();
                    currenty++;
                }
            }
            if(legalLeft(x, y, color)) {
                currentx = x-1;
                while(getPiece(currentx, y).getColor().compare(color) != 0) {
                    list.at(getIndex(currentx, y)).flip();
                    currentx--;
                }
            }
            if(legalRight(x, y, color)) {
                currentx = x+1;
                while(getPiece(currentx, y).getColor().compare(color) != 0) {
                    list.at(getIndex(currentx, y)).flip();
                    currentx++;
                }
            }
            if(legalUpLeft(x, y, color)) {
                currentx = x-1;
                currenty = y+1;
                while(getPiece(currentx, currenty).getColor().compare(color) != 0) {
                    list.at(getIndex(currentx, currenty)).flip();
                    currentx--;
                    currenty++;
                }
            }
            if(legalUpRight(x, y, color)) {
                currentx = x+1;
                currenty = y+1;
                while(getPiece(currentx, currenty).getColor().compare(color) != 0) {
                    list.at(getIndex(currentx, currenty)).flip();
                    currentx++;
                    currenty++;
                }
            }
            if(legalDownRight(x, y, color)) {
                currentx = x+1;
                currenty = y-1;
                while(getPiece(currentx, currenty).getColor().compare(color) != 0) {
                    list.at(getIndex(currentx, currenty)).flip();
                    currentx++;
                    currenty--;
                }
            }
            if(legalDownLeft(x, y, color)) {
                currentx = x-1;
                currenty = y-1;
                while(getPiece(currentx, currenty).getColor().compare(color) != 0) {
                    list.at(getIndex(currentx, currenty)).flip();
                    currentx--;
                    currenty--;
                }
            }
            list.push_back(Piece(x, y, color));
        }
        bool checkLegal(string color) {         ///Checks if legal move exists for specific color
            for (int x=1; x<=8; x++) {
                for (int y=1; y<=8; y++) {
                    if (legalMove(x, y, color)) {return true;}
                }
            }
            return false;
        }
    public:
        Board() {
            ///Initial board state
            list.push_back(Piece(4, 4, "black"));
            list.push_back(Piece(5, 5, "black"));
            list.push_back(Piece(4, 5, "white"));
            list.push_back(Piece(5, 4, "white"));
        }
        void execute() {
            int turn = 1;
            int gameOver = 0;
            string col[2] = {"white", "black"};
            do {
                bool first = true;
                int x, y;

                ///Game loop
                while(!legalMove(x, y, col[turn]) || first) {
                    system("cls");
                    display();
                    cout << col[turn] << "'s turn" << endl << endl;
                    if(!legalMove(x, y, col[turn]) && !first) {
                        cout << "Illegal move" << endl;
                    }
                    cout << "X: ";
                    cin >> x;
                    cout << "Y: " ;
                    cin >> y;
                    first = false;
                }
                placePiece(x, y, col[turn]);

                if (checkLegal(col[(turn+1)%2])) {
                    turn = (turn+1)%2;
                }
            } while (checkLegal("white") || checkLegal("black"));

            ///Win Screen
            system("cls");
            display();
            cout << "Game over" << endl;
            cout << "Black pieces: " << getBlackNum() << endl;
            cout << "White pieces: " << getWhiteNum() << endl;
            if (getBlackNum() > getWhiteNum()) {
                cout << "Black wins" << endl;
            } else if (getBlackNum() == getWhiteNum()) {
                cout << "Tie" << endl;
            } else {
                cout << "White wins" << endl;
            }
        }
};

int main() {
    Board b;
    b.execute();

    return 0;
}
