package com.example.button;
import android.os.AsyncTask;

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;

public class SendData extends AsyncTask<String, Void, Void>{
    private Exception exception;
    @Override
    protected Void doInBackground(String... params){
        try{
            try{
                Socket socket = new Socket("172.20.10.7",8001);
                PrintWriter outToServer= new PrintWriter(
                        new OutputStreamWriter(
                                socket.getOutputStream()));
                outToServer.print(params[0]);
                outToServer.flush();
            }catch (IOException e){
                e.printStackTrace();
            }
        }catch (Exception e)
        {
            this.exception = e;
            return null;
        }
        return null;
    }
}
