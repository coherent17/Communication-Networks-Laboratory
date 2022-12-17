package com.example.lab3_set;
import android.os.Bundle;
import android.os.SystemClock;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.Chronometer;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

public class stopwatch_fragment extends Fragment {
    private
    View root;
    Button start_btn;
    Button stop_btn;
    Chronometer chronometer;

    @Nullable
    @Override
    public View onCreateView(@NonNull @org.jetbrains.annotations.NotNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        root =  inflater.inflate(R.layout.stopwatch_fragment, container, false);
        chronometer = (Chronometer) root.findViewById(R.id.chronometer);
        start_btn = (Button) root.findViewById(R.id.start_btn);
        stop_btn = (Button) root.findViewById(R.id.stop_btn);

        start_btn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                chronometer.setBase(SystemClock.elapsedRealtime());
                chronometer.start();
            }
        });

        stop_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                chronometer.stop();
            }
        });

        chronometer.setOnChronometerTickListener(new Chronometer.OnChronometerTickListener() {
            @Override
            public void onChronometerTick(Chronometer chronometer) {
                long time = SystemClock.elapsedRealtime() - chronometer.getBase();
                int s = (int)time / 1000;       //ms -> s
                int m = (int) s / 60;           //sec -> min
                int h = (int) m / 60;           //min -> hour
                s = s - m * 60;                 
                m = m - h * 60;
                chronometer.setText(String.format("%02d:%02d:%02d", h, m, s));
            }
        });
        return root;
    }
}
