﻿#Creating PSobject model with information properties of a new user.
#These informations should be provided by HR departement
#Import all the command module fo managing active directory
#Import-Module ActiveDirectory

#Import all the command module fo managing active directory
#ConnectAD.ps1
#Connect to your Domain Controller(DC)
#Change the value after the -ComputerName to your know DC

#$session = New-PSSession -ComputerName "VWSERVDCSH" -Credential (Get-Credential)
#Invoke-Command $session -Scriptblock { Import-Module ActiveDirectory }
#Import-PSSession -Session $session -module ActiveDirectory

#describe the properties of User object
$Userclass = New-Object psobject -Property @{
    first_name = $null
    last_name = $null
    login = $null
    Tel_number = $null
    mail_address = $null
    departement = $null
    function = $null
}

#Contructor of object new user
#define the mandatory information parameters of the object
function Userclass {
    param(
        [Parameter(Mandatory=$true)]
        [String]$first_name,
        [Parameter(Mandatory=$true)]
        [string]$last_name,
        [parameter(Mandatory=$true)]
        [string]$login,
        [Parameter(Mandatory=$false)]
        [long]$Tel_number,
        [Parameter(Mandatory=$true)]
        [string]$mail_address,
        [Parameter(Mandatory=$true)]
        #[ValidateSet('CA','Treasury','IT','Finance')]
        [String]$departement,
        [Parameter(Mandatory=$true)]
        #[ValidateSet('IT','Accountant','VP','AVP')]
        [string]$function
    )
    $Userclass = $Userclass.psobject.copy()
    $Userclass.first_name = $first_name
    $Userclass.last_name = $last_name
    $Userclass.login = $login
    $Userclass.Tel_number = $Tel_number
    $Userclass.mail_address = $mail_address
    $Userclass.departement = $departement
    $Userclass.function = $Function
    $Userclass
}

echo "la class userclass définissant un utilisateur de l'AD est défini"



#connexion to the Active directory and create users

#connecting to the active directoru with the service account
Enter-PSSession -ComputerName VWSERVDCSH.silver-holdings.lan -Credential Silver-Holdings\svc_create_user

$New_User = Userclass -first_name Jean -last_name Dupont -login je.du -Tel_number 0000 -mail_address art@mail.com -departement CA -function VP


#verifier qu'il n'existe pas de user déjà crée avec le $New_

#Creating the user to the Active Directory
New-ADUser -Name $New_User.first_name -GivenName $New_User.first_name -Surname $New_User.lastname  -Department $New_User.departement -Description $New_User.function -OfficePhone $New_User.Tel_number -SamAccountName $New_User.login -EmailAddress $New_User.mail_address -path "OU=Laptop Users,OU=Users,OU=SH,DC=silver-holdings,DC=lan" -AccountPassword (ConvertTo-SecureString "Welcome.2019" -AsPlainText -force) -PassThru -Enabled $true
