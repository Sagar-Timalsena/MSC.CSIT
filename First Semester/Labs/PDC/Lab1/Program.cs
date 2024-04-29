using System.Security.Cryptography;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        string originalFilePath = "original_file.txt";
        string splitFilesDirectory = "split_files";
        string encryptedFilesDirectory = "encrypted_files";
        string mergedEncryptedFilePath = "encrypted_merged_file.txt";
        long fileSizeInBytes = 2L * 1024 * 1024 * 1024; // 2 GB

        // Generate original text file
        GenerateTextFile(originalFilePath, fileSizeInBytes);

        // Split original file into multiple files
        SplitFile(originalFilePath, splitFilesDirectory);

        // Encrypt split files
        EncryptFiles(splitFilesDirectory, encryptedFilesDirectory);

        // Merge encrypted files into one
        MergeFiles(encryptedFilesDirectory, mergedEncryptedFilePath);

        Console.WriteLine("Process completed successfully.");
    }

    static void GenerateTextFile(string filePath, long fileSizeInBytes)
    {
        using (StreamWriter writer = new StreamWriter(filePath))
        {
            writer.Write(RandomString(fileSizeInBytes));
        }
    }

    static string RandomString(long length)
    {
        const string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        StringBuilder sb = new StringBuilder((int)length);
        Random random = new Random();
        for (long i = 0; i < length; i++)
        {
            sb.Append(chars[random.Next(chars.Length)]);
        }
        return sb.ToString();
    }

    static void SplitFile(string originalFilePath, string splitFilesDirectory)
    {
        if (!Directory.Exists(splitFilesDirectory))
            Directory.CreateDirectory(splitFilesDirectory);

        using (FileStream inputStream = File.OpenRead(originalFilePath))
        {
            int splitSize = 1024 * 1024 * 100; // 100 MB per file
            byte[] buffer = new byte[splitSize];
            int bytesRead;
            int index = 0;

            while ((bytesRead = inputStream.Read(buffer, 0, buffer.Length)) > 0)
            {
                string splitFileName = Path.Combine(splitFilesDirectory, $"split_{index}.txt");
                using (FileStream outputStream = File.Create(splitFileName))
                {
                    outputStream.Write(buffer, 0, bytesRead);
                }
                index++;
            }
        }
    }

    static void EncryptFiles(string inputDirectory, string outputDirectory)
    {
        if (!Directory.Exists(outputDirectory))
            Directory.CreateDirectory(outputDirectory);

        foreach (string inputFile in Directory.GetFiles(inputDirectory))
        {
            string outputFile = Path.Combine(outputDirectory, Path.GetFileName(inputFile));
            using (Aes aes = Aes.Create())
            {
                aes.GenerateKey();
                aes.GenerateIV();

                using (FileStream inputStream = File.OpenRead(inputFile))
                using (FileStream outputStream = File.Create(outputFile))
                using (CryptoStream cryptoStream = new CryptoStream(outputStream, aes.CreateEncryptor(), CryptoStreamMode.Write))
                {
                    inputStream.CopyTo(cryptoStream);
                }
            }
        }
    }

    static void MergeFiles(string inputDirectory, string mergedFilePath)
    {
        using (FileStream outputStream = File.Create(mergedFilePath))
        {
            foreach (string inputFile in Directory.GetFiles(inputDirectory))
            {
                using (FileStream inputStream = File.OpenRead(inputFile))
                {
                    inputStream.CopyTo(outputStream);
                }
            }
        }
    }
}
