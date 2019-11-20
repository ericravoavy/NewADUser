#Creating PSobject model with information properties of a new employee.
#These informations should be provided by HR departement

#Import all the command module fo managing active directory
#ConnectAD.ps1
#Connect to your Domain Controller(DC)
#Change the value after the -ComputerName to your know DC

#$session = New-PSSession -ComputerName "VWSERVDCSH" -Credential (Get-Credential)
#Invoke-Command $session -Scriptblock { Import-Module ActiveDirectory }
#Import-PSSession -Session $session -module ActiveDirectory

#describe the properties of Userclass object
$Userclass = New-Object psobject -Property @{
    first_name = $null
    last_name = $null
    login = $null
    Tel_number = $null
    mail_address = $null
    departement = $null
    function = $null
    OUPath = $null
    Enable = $null
}

#Contructor of userclass class
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
        [string]$function,
        [Parameter(Mandatory=$true)]
        [string]$OUPath,
        [Parameter(Mandatory=$true)]
        [string]$Enable
    )
    $Userclass = $Userclass.psobject.copy()
    $Userclass.first_name = $first_name
    $Userclass.last_name = $last_name
    $Userclass.login = $login
    $Userclass.Tel_number = $Tel_number
    $Userclass.mail_address = $mail_address
    $Userclass.departement = $departement
    $Userclass.function = $Function
    $userclass.OUPath = $OUPath
    $userclass.Enable = $Enable
    $Userclass
}

echo "la class userclass définissant un utilisateur de l'AD est défini"


#Initiate an user from class Userclass
$New_User = Userclass -first_name Jean -last_name Alvin -login je.du -Tel_number 063243567 -mail_address art@mail.com -departement CA -function VP -OUPath "OU=Laptop Users,OU=Users,OU=SH,DC=silver-holdings,DC=lan" -Enable "$true"

#display the new User created
echo $New_User

#connecting to the active directory with the service account

#$Password = ConvertTo-SecureString "Password" -AsPlainText -Force
#$cred = New-Object System.Management.Automation.PSCredential ("silver-holdings.lan\svc_create_user", $Password)
#Enter-PSSession –ComputerName VWSERVDCSH.silver-holdings.lan –Credential $cred

#connexion to the Active directory and create users

New-ADUser -Name $New_User.first_name -GivenName $New_User.first_name -Surname $New_User.lastname  -Department $New_User.departement -Description $New_User.function -OfficePhone $New_User.Tel_number -SamAccountName $New_User.login -EmailAddress $New_User.mail_address -Path $New_User.OUPath -AccountPassword (ConvertTo-SecureString "Welcome.2019" -AsPlainText -force) -PassThru -Enabled $true

#verifier qu'il n'existe pas de user déjà crée avec le $New_

#if (@(Get-ADUser -Filter { SamAccountName -eq $New_User.login }).Count -eq 0) {
#    Write-Warning -Message "User does not exist"
#    New-ADUser -Name $New_User.first_name -GivenName $New_User.first_name -Surname $New_User.lastname  -Department $New_User.departement -Description $New_User.function -OfficePhone $New_User.Tel_number -SamAccountName $New_User.login -EmailAddress $New_User.mail_address -Path $New_User.OUPath -AccountPassword (ConvertTo-SecureString "Welcome.2019" -AsPlainText -force) -PassThru -Enabled $true
#    }
#else#
#    {
#    Write-Warning -Message "User exist"
#    }


#-SearchBase $New_User.OUPath

#if($TestUser.SamAccountName -eq $null){
#    echo "User n'existe pas"
    #Creating the user to the Active Directory
    #New-ADUser -Name $New_User.first_name -GivenName $New_User.first_name -Surname $New_User.lastname  -Department $New_User.departement -Description $New_User.function -OfficePhone $New_User.Tel_number -SamAccountName $New_User.login -EmailAddress $New_User.mail_address -Path $New_User.OUPath -AccountPassword (ConvertTo-SecureString "Welcome.2019" -AsPlainText -force) -PassThru -Enabled $true
#}
#Else
#{
#    echo "User existe déjà"
#}


#verifier qu'il n'existe pas de user déjà crée avec le $New_