clear;
clc;

Load_C = input('请输入受压时的荷载');
Load_T = input('请输入受拉时的荷载');

URX1_C = input('请输入左上角受压时X方向的转角');
URX1_T = input('请输入左上角受拉时X方向的转角');
URY1_C = input('请输入左上角受压时Y方向的转角');
URY1_T = input('请输入左上角受拉时Y方向的转角');
URZ1_C = input('请输入左上角受压时Z方向的转角');
URZ1_T = input('请输入左上角受拉时Z方向的转角');

URX2_C = input('请输入顶边中点受压时X方向的转角');
URX2_T = input('请输入顶边中点受拉时X方向的转角');
URY2_C = input('请输入顶边中点受压时Y方向的转角');
URY2_T = input('请输入顶边中点受拉时Y方向的转角');
URZ2_C = input('请输入顶边中点受压时Z方向的转角');
URZ2_T = input('请输入顶边中点受拉时Z方向的转角');

URX3_C = input('请输入右上角受压时X方向的转角');
URX3_T = input('请输入右上角受拉时X方向的转角');
URY3_C = input('请输入右上角受压时Y方向的转角');
URY3_T = input('请输入右上角受拉时Y方向的转角');
URZ3_C = input('请输入右上角受压时Z方向的转角');
URZ3_T = input('请输入右上角受拉时Z方向的转角');

URX4_C = input('请输入左边中点受压时X方向的转角');
URX4_T = input('请输入左边中点受拉时X方向的转角');
URY4_C = input('请输入左边中点受压时Y方向的转角');
URY4_T = input('请输入左边中点受拉时Y方向的转角');
URZ4_C = input('请输入左边中点受压时Z方向的转角');
URZ4_T = input('请输入左边中点受拉时Z方向的转角');

URX5_C = input('请输入面板中点受压时X方向的转角');
URX5_T = input('请输入面板中点受拉时X方向的转角');
URY5_C = input('请输入面板中点受压时Y方向的转角');
URY5_T = input('请输入面板中点受拉时Y方向的转角');
URZ5_C = input('请输入面板中点受压时Z方向的转角');
URZ5_T = input('请输入面板中点受拉时Z方向的转角');

URX6_C = input('请输入右边中点受压时X方向的转角');
URX6_T = input('请输入右边中点受拉时X方向的转角');
URY6_C = input('请输入右边中点受压时Y方向的转角');
URY6_T = input('请输入右边中点受拉时Y方向的转角');
URZ6_C = input('请输入右边中点受压时Z方向的转角');
URZ6_T = input('请输入右边中点受拉时Z方向的转角');

URX7_C = input('请输入左下角受压时X方向的转角');
URX7_T = input('请输入左下角受拉时X方向的转角');
URY7_C = input('请输入左下角受压时Y方向的转角');
URY7_T = input('请输入左下角受拉时Y方向的转角');
URZ7_C = input('请输入左下角受压时Z方向的转角');
URZ7_T = input('请输入左下角受拉时Z方向的转角');

URX8_C = input('请输入底边中点受压时X方向的转角');
URX8_T = input('请输入底边中点受拉时X方向的转角');
URY8_C = input('请输入底边中点受压时Y方向的转角');
URY8_T = input('请输入底边中点受拉时Y方向的转角');
URZ8_C = input('请输入底边中点受压时Z方向的转角');
URZ8_T = input('请输入底边中点受拉时Z方向的转角');

URX9_C = input('请输入右下角受压时X方向的转角');
URX9_T = input('请输入右下角受拉时X方向的转角');
URY9_C = input('请输入右下角受压时Y方向的转角');
URY9_T = input('请输入右下角受拉时Y方向的转角');
URZ9_C = input('请输入右下角受压时Z方向的转角');
URZ9_T = input('请输入右下角受拉时Z方向的转角');

Frequency_1 = input('请输入一阶频率');
Frequency_2 = input('请输入二阶频率');
Frequency_3 = input('请输入三阶频率');
Frequency_4 = input('请输入四阶频率');

P = [ (URX1_T/Load_T)/(URX1_C/Load_C),(URY1_T/Load_T)/(URY1_C/Load_C),(URZ1_T/Load_T)/(URZ1_C/Load_C), ...
      (URX2_T/Load_T)/(URX2_C/Load_C),(URY2_T/Load_T)/(URY2_C/Load_C),(URZ2_T/Load_T)/(URZ2_C/Load_C), ...
      (URX3_T/Load_T)/(URX3_C/Load_C),(URY3_T/Load_T)/(URY3_C/Load_C),(URZ3_T/Load_T)/(URZ3_C/Load_C), ...
      (URX4_T/Load_T)/(URX4_C/Load_C),(URY4_T/Load_T)/(URY4_C/Load_C),(URZ4_T/Load_T)/(URZ4_C/Load_C), ...
      (URX5_T/Load_T)/(URX5_C/Load_C),(URY5_T/Load_T)/(URY5_C/Load_C),(URZ5_T/Load_T)/(URZ5_C/Load_C), ...
      (URX6_T/Load_T)/(URX6_C/Load_C),(URY6_T/Load_T)/(URY6_C/Load_C),(URZ6_T/Load_T)/(URZ6_C/Load_C), ...
      (URX7_T/Load_T)/(URX7_C/Load_C),(URY7_T/Load_T)/(URY7_C/Load_C),(URZ7_T/Load_T)/(URZ7_C/Load_C), ...
      (URX8_T/Load_T)/(URX8_C/Load_C),(URY8_T/Load_T)/(URY8_C/Load_C),(URZ8_T/Load_T)/(URZ8_C/Load_C), ...
      (URX9_T/Load_T)/(URX9_C/Load_C),(URY9_T/Load_T)/(URY9_C/Load_C),(URZ9_T/Load_T)/(URZ9_C/Load_C), ...
      Frequency_1, Frequency_2, Frequency_3, Frequency_4]';

load('BPnet2');

T = sim(net,P);
T = round(T)
if T(1) == 1
    '顶边第一单元脱胶'
    a(1) = 1;
elseif T(1) == 3
    '顶边第二单元脱胶'
    a(1) = 1;
elseif T(1) == 5
    '顶边第三单元脱胶'
    a(1) = 1;
elseif T(1) == 4
    '顶边第一、第二单元脱胶'
    a(1) = 2;
elseif T(1) == 6
    '顶边第一、第三单元脱胶'
    a(1) = 2;
elseif T(1) == 8
    '顶边第二、第三单元脱胶'
    a(1) = 2;
elseif T(1) == 9
    '顶边全部脱胶'
    a(1) = 3;
else
    '顶边未脱胶'
    a(1) = 0;
end
    
if T(2) == 1
    '右边第一单元脱胶'
    a(2) = 1;
elseif T(2) == 3
    '右边第二单元脱胶'
    a(2) = 1;
elseif T(2) == 5
    '右边第三单元脱胶'
    a(2) = 1;
elseif T(2) == 4
    '右边第一、第二单元脱胶'
    a(2) = 2;
elseif T(2) == 6
    '右边第一、第三单元脱胶'
    a(2) = 2;
elseif T(2) == 8
    '右边第二、第三单元脱胶'
    a(2) = 2;
elseif T(2) == 9
    '右边全部脱胶'
    a(2) = 3;
else
    '右边未脱胶'
    a(2) = 0;
end 

if T(3) == 1
    '底边第一单元脱胶'
    a(3) = 1;
elseif T(3) == 3
    '底边第二单元脱胶'
    a(3) = 1;
elseif T(3) == 5
    '底边第三单元脱胶'
    a(3) = 1;
elseif T(3) == 4
    '底边第一、第二单元脱胶'
    a(3) = 2;
elseif T(3) == 6
    '底边第一、第三单元脱胶'
    a(3) = 2;
elseif T(3) == 8
    '底边第二、第三单元脱胶'
    a(3) = 2;
elseif T(3) == 9
    '底边全部脱胶'
    a(3) = 3;
else
    '底边未脱胶'
    a(3) = 0;
end

if T(4) == 1
    '左边第一单元脱胶'
    a(4) = 1;
elseif T(4) == 3
    '左边第二单元脱胶'
    a(4) = 1;
elseif T(4) == 5
    '左边第三单元脱胶'
    a(4) = 1;
elseif T(4) == 4
    '左边第一、第二单元脱胶'
    a(4) = 2;
elseif T(4) == 6
    '左边第一、第三单元脱胶'
    a(4) = 2;
elseif T(4) == 8
    '左边第二、第三单元脱胶'
    a(4) = 2;
elseif T(4) == 9
    '左边全部脱胶'
    a(4) = 3;
else
    '左边未脱胶'
    a(4) = 0;
end

b = (a(1)+a(2)+a(3)+a(4))/12;

if b>=0.3 & b<0.5
    '玻璃处于较危险状态'
elseif b>=0.5
    '玻璃处于严重危险状态'
else
    '玻璃处于安全状态'
end