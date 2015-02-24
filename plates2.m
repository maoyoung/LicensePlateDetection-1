%ImageFiles = dir('/Users/msit/Desktop/Cropped Plates/*.jpg');
ImageFiles = dir('/home/senseable-beast/Downloads/Cropped Plates/*.jpg');
disp(size(ImageFiles,1)); %66 found images

for Index = 1:size(ImageFiles,1)
    
    
%     counter = 1;
    %name(Index) = ImageFiles(Index).name;
%     varname = ImageFiles(Index).name;
    
    eval([strcat('varname_', num2str(Index), '= imread(ImageFiles(Index).name);')]);
%     eval([strcat(varname, '= imread(ImageFiles(Index).name);')]);
    %     varname  = imread(ImageFiles(Index).name);
    %name(Index) = imread(ImageFiles(Index).name);
%     counter = counter +1;
    %size(counter)
    
    disp('about to save');
    if Index == 1
        save('plates2.mat', strcat('varname_', num2str(Index)));
    else
        save('plates2.mat', strcat('varname_', num2str(Index)), '-append');
    end
    disp('saved');
end

A = imread('DSCN0408.jpg');
% save('plates2.mat', 'A');
% B = imread ('DSCN0410.jpg');
% save('plates2.mat', 'B', '-append');

% for Index = 1:length(ImageFiles)
%     Index = imread(ImageFiles(Index).name);
%     %disp(Index);
%     %save('plates2.mat', ImageFiles, '-append');
% end
disp('loading');
whos('-file','plates2.mat');
disp('finished loading');
