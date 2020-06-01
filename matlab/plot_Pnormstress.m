clear all
exp='26'
fileinfo=['2002_01_01_12_30_k0009.',exp];
file1=['sig1norm',fileinfo];
file2=['sig2norm',fileinfo];

%fileI=['sigInormEVP', fileinfo]
%fileII=['sigIInormEVP',fileinfo]


sig1=load(file1);
sig2=load(file2);

%load sigInorm1990_01_01_06_00_k0009.18
%sigI=sigInorm1990_01_01_06_00_k0009;

%load sigIInorm1990_01_01_06_00_k0009.18
%sigII=sigIInorm1990_01_01_06_00_k0009;

Deltax = 10;

if Deltax == 10
nx    = 518;                 % x-dim of the domain
ny    = 438;                 % y-dim of the domain
end


k=1
for j=1:ny 
for i= 1:nx

if (sig1(j,i) > -100)
k=k+1;
sig1p(k)=sig1(j,i);
sig2p(k)=sig2(j,i);
l1(k)=0.0;
end

end
end

kk=k

re=0.5;
dx=0.001;

for l=1:1000
x(l)=(l-1)*dx;
sigIIE(l)=0.5d0*(sqrt((re^2-(x(l)-re)^2)));

end

max(sig1p)
max(sig2p)

%figure(1)
%plot(sigIp, sigIIp, '.')
clear figure(2)
figure(3)
%scatter(sig1p, sig2p, 'Marker', 'o', 'MarkerSize', 4)
%plot(sig1p, l1, 'k-')
%hold on
%plot(sig2p, l1, 'k-')
%hold on

%refline(1,1)
%hold on

%plot(sig1p, sig2p, '.', 'MarkerSize', 5)'Marker', 'o', 'MarkerSize', 4,
%plot(x, sigIIE,'k')
%axis([-0.1 1.1 0 0.3])
c1=ezplot('(x+y+1)^2+4*(x-y)^2 = 1');set(c1,'linestyle','-', 'linewidth',1,'Color', [0.5 0.5 0.5]);
hold on
x = [0 0];
y = [0.2 -1.2];
line(x,y,'Color','k','LineStyle','--')

x = [0.2 -1.2];
y = [0 0];
line(x,y,'Color','k','LineStyle','--')


plot(sig1p, sig2p, 'o', 'MarkerSize', 3)
hold on
c1=ezplot('(x+y+1)^2+4*(x-y)^2 = 1');set(c1,'linestyle','-', 'linewidth',1,'Color', [0.5 0.5 0.5]);
set(gca,'fontsize',14)

axis([-1.2 0.2 -1.2 0.2])
%xlabel('\sigma_1/P_p')
%ylabel('\sigma_2/P_p')
%xlabel('\sigma_1/P_p', 'FontSize', 16)
%ylabel('\sigma_2/P_p', 'FontSize', 16)
xlabel('\sigma_1/P', 'FontSize', 16)
ylabel('\sigma_2/P', 'FontSize', 16)
axis square
title('')

%figure(3)
%c1=ezplot('(x+y+1)^2+4*(x-y)^2 = 1');set(c1,'linestyle','-', 'linewidth',2,'Color', 'k');

fileout=['norm_stresses_exp_', exp];

print(fileout,'-dpng')

%print ("norm_stress_exp18.png", "-dpng"); %octave stuff
