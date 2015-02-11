ListofPlates = {};
ImagesToSave = struct();
ImageFiles = dir(['./' '*.*']);
disp(length(ImageFiles));
for Index = 1:length(ImageFiles)
    disp('found an image');
    baseFileName = ImageFiles(Index).name;
    [folder, name, extension] = fileparts(baseFileName);
    extension = upper(extension);
    switch lower (extension)
        case {'.jpg'}
            ListOfImageNames = [ListOfImageNames baseFileName];
            ImagesToSave.(name) = imread(baseFileName);
        otherwise
    end
end
save ('plates.mat', '-struct','ImagesToSave');
