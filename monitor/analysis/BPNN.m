clear;
clc;

Load_C = input('��������ѹʱ�ĺ���');
Load_T = input('����������ʱ�ĺ���');

URX1_C = input('���������Ͻ���ѹʱX�����ת��');
URX1_T = input('���������Ͻ�����ʱX�����ת��');
URY1_C = input('���������Ͻ���ѹʱY�����ת��');
URY1_T = input('���������Ͻ�����ʱY�����ת��');
URZ1_C = input('���������Ͻ���ѹʱZ�����ת��');
URZ1_T = input('���������Ͻ�����ʱZ�����ת��');

URX2_C = input('�����붥���е���ѹʱX�����ת��');
URX2_T = input('�����붥���е�����ʱX�����ת��');
URY2_C = input('�����붥���е���ѹʱY�����ת��');
URY2_T = input('�����붥���е�����ʱY�����ת��');
URZ2_C = input('�����붥���е���ѹʱZ�����ת��');
URZ2_T = input('�����붥���е�����ʱZ�����ת��');

URX3_C = input('���������Ͻ���ѹʱX�����ת��');
URX3_T = input('���������Ͻ�����ʱX�����ת��');
URY3_C = input('���������Ͻ���ѹʱY�����ת��');
URY3_T = input('���������Ͻ�����ʱY�����ת��');
URZ3_C = input('���������Ͻ���ѹʱZ�����ת��');
URZ3_T = input('���������Ͻ�����ʱZ�����ת��');

URX4_C = input('����������е���ѹʱX�����ת��');
URX4_T = input('����������е�����ʱX�����ת��');
URY4_C = input('����������е���ѹʱY�����ת��');
URY4_T = input('����������е�����ʱY�����ת��');
URZ4_C = input('����������е���ѹʱZ�����ת��');
URZ4_T = input('����������е�����ʱZ�����ת��');

URX5_C = input('����������е���ѹʱX�����ת��');
URX5_T = input('����������е�����ʱX�����ת��');
URY5_C = input('����������е���ѹʱY�����ת��');
URY5_T = input('����������е�����ʱY�����ת��');
URZ5_C = input('����������е���ѹʱZ�����ת��');
URZ5_T = input('����������е�����ʱZ�����ת��');

URX6_C = input('�������ұ��е���ѹʱX�����ת��');
URX6_T = input('�������ұ��е�����ʱX�����ת��');
URY6_C = input('�������ұ��е���ѹʱY�����ת��');
URY6_T = input('�������ұ��е�����ʱY�����ת��');
URZ6_C = input('�������ұ��е���ѹʱZ�����ת��');
URZ6_T = input('�������ұ��е�����ʱZ�����ת��');

URX7_C = input('���������½���ѹʱX�����ת��');
URX7_T = input('���������½�����ʱX�����ת��');
URY7_C = input('���������½���ѹʱY�����ת��');
URY7_T = input('���������½�����ʱY�����ת��');
URZ7_C = input('���������½���ѹʱZ�����ת��');
URZ7_T = input('���������½�����ʱZ�����ת��');

URX8_C = input('������ױ��е���ѹʱX�����ת��');
URX8_T = input('������ױ��е�����ʱX�����ת��');
URY8_C = input('������ױ��е���ѹʱY�����ת��');
URY8_T = input('������ױ��е�����ʱY�����ת��');
URZ8_C = input('������ױ��е���ѹʱZ�����ת��');
URZ8_T = input('������ױ��е�����ʱZ�����ת��');

URX9_C = input('���������½���ѹʱX�����ת��');
URX9_T = input('���������½�����ʱX�����ת��');
URY9_C = input('���������½���ѹʱY�����ת��');
URY9_T = input('���������½�����ʱY�����ת��');
URZ9_C = input('���������½���ѹʱZ�����ת��');
URZ9_T = input('���������½�����ʱZ�����ת��');

Frequency_1 = input('������һ��Ƶ��');
Frequency_2 = input('���������Ƶ��');
Frequency_3 = input('����������Ƶ��');
Frequency_4 = input('�������Ľ�Ƶ��');

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
    '���ߵ�һ��Ԫ�ѽ�'
    a(1) = 1;
elseif T(1) == 3
    '���ߵڶ���Ԫ�ѽ�'
    a(1) = 1;
elseif T(1) == 5
    '���ߵ�����Ԫ�ѽ�'
    a(1) = 1;
elseif T(1) == 4
    '���ߵ�һ���ڶ���Ԫ�ѽ�'
    a(1) = 2;
elseif T(1) == 6
    '���ߵ�һ��������Ԫ�ѽ�'
    a(1) = 2;
elseif T(1) == 8
    '���ߵڶ���������Ԫ�ѽ�'
    a(1) = 2;
elseif T(1) == 9
    '����ȫ���ѽ�'
    a(1) = 3;
else
    '����δ�ѽ�'
    a(1) = 0;
end
    
if T(2) == 1
    '�ұߵ�һ��Ԫ�ѽ�'
    a(2) = 1;
elseif T(2) == 3
    '�ұߵڶ���Ԫ�ѽ�'
    a(2) = 1;
elseif T(2) == 5
    '�ұߵ�����Ԫ�ѽ�'
    a(2) = 1;
elseif T(2) == 4
    '�ұߵ�һ���ڶ���Ԫ�ѽ�'
    a(2) = 2;
elseif T(2) == 6
    '�ұߵ�һ��������Ԫ�ѽ�'
    a(2) = 2;
elseif T(2) == 8
    '�ұߵڶ���������Ԫ�ѽ�'
    a(2) = 2;
elseif T(2) == 9
    '�ұ�ȫ���ѽ�'
    a(2) = 3;
else
    '�ұ�δ�ѽ�'
    a(2) = 0;
end 

if T(3) == 1
    '�ױߵ�һ��Ԫ�ѽ�'
    a(3) = 1;
elseif T(3) == 3
    '�ױߵڶ���Ԫ�ѽ�'
    a(3) = 1;
elseif T(3) == 5
    '�ױߵ�����Ԫ�ѽ�'
    a(3) = 1;
elseif T(3) == 4
    '�ױߵ�һ���ڶ���Ԫ�ѽ�'
    a(3) = 2;
elseif T(3) == 6
    '�ױߵ�һ��������Ԫ�ѽ�'
    a(3) = 2;
elseif T(3) == 8
    '�ױߵڶ���������Ԫ�ѽ�'
    a(3) = 2;
elseif T(3) == 9
    '�ױ�ȫ���ѽ�'
    a(3) = 3;
else
    '�ױ�δ�ѽ�'
    a(3) = 0;
end

if T(4) == 1
    '��ߵ�һ��Ԫ�ѽ�'
    a(4) = 1;
elseif T(4) == 3
    '��ߵڶ���Ԫ�ѽ�'
    a(4) = 1;
elseif T(4) == 5
    '��ߵ�����Ԫ�ѽ�'
    a(4) = 1;
elseif T(4) == 4
    '��ߵ�һ���ڶ���Ԫ�ѽ�'
    a(4) = 2;
elseif T(4) == 6
    '��ߵ�һ��������Ԫ�ѽ�'
    a(4) = 2;
elseif T(4) == 8
    '��ߵڶ���������Ԫ�ѽ�'
    a(4) = 2;
elseif T(4) == 9
    '���ȫ���ѽ�'
    a(4) = 3;
else
    '���δ�ѽ�'
    a(4) = 0;
end

b = (a(1)+a(2)+a(3)+a(4))/12;

if b>=0.3 & b<0.5
    '�������ڽ�Σ��״̬'
elseif b>=0.5
    '������������Σ��״̬'
else
    '�������ڰ�ȫ״̬'
end